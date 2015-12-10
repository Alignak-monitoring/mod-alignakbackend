#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2015-2015: Alignak team, see AUTHORS.txt file for contributors
#
# This file is part of Alignak.
#
# Alignak is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Alignak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Alignak.  If not, see <http://www.gnu.org/licenses/>.
"""
This module is used to get configuration from alignak-backend with arbiter
"""

import time
from alignak_backend_client.client import Backend
# pylint: disable=F0401
from alignak.basemodule import BaseModule
# pylint: disable=F0401
from alignak.log import logger


# pylint: disable=C0103
properties = {
    'daemons': ['arbiter'],
    'type': 'alignakbackendarbit',
    'external': False,
    'phases': ['configuration'],
    }


def get_instance(mod_conf):
    """Return a module instance for the plugin manager

    :param mod_conf: Configuration object
    :type mod_conf: object
    :return: AlignakBackendArbit instance
    :rtype: object
    """
    logger.info("[Backend Arbiter] Get a Alignak config module for plugin %s",
                mod_conf.get_name())
    instance = AlignakBackendArbit(mod_conf)
    return instance


class AlignakBackendArbit(BaseModule):
    """ This class is used to get configuration from alignak-backend
    """

    def __init__(self, modconf):
        BaseModule.__init__(self, modconf)
        self.url = getattr(modconf, 'api_url', 'http://localhost:5000')
        self.backend = Backend(self.url)
        self.backend.token = getattr(modconf, 'token', '')
        if self.backend.token == '':
            self.getToken(getattr(modconf, 'username', ''), getattr(modconf, 'password', ''),
                          getattr(modconf, 'allowgeneratetoken', False))

        self.configraw = {}
        self.config = {'commands': [],
                       'timeperiods': [],
                       'hosts': [],
                       'hostgroups': [],
                       'services': [],
                       'contacts': []}

    # Common functions
    def do_loop_turn(self):
        """This function is called/used when you need a module with
        a loop function (and use the parameter 'external': True)
        """
        logger.info("[Backend Arbiter] In loop")
        time.sleep(1)

    def getToken(self, username, password, generatetoken):
        """
        Authenticate and get the token

        :param username: login name
        :type username: str
        :param password: password
        :type password: str
        :param generatetoken: if True allow generate token, otherwise not generate
        :type generatetoken: bool
        :return: None
        """
        generate = 'enabled'
        if not generatetoken:
            generate = 'disabled'
        self.backend.login(username, password, generate)

    def single_relation(self, resource, mapping, ctype):
        """
        Convert single embedded data to name of relation_data
        Example:
        {'contacts': {'_id': a3659204fe,'name':'admin'}}
        converted to:
        {'contacts': 'admin'}

        :param resource: dictionary got from alignak-backend
        :type resource: dict
        :param mapping: key value of resource
        :type mapping: str
        :param ctype: type of configraw (hosts, services, commands...)
        :type ctype: str
        """
        if mapping in resource:
            if resource[mapping] is not None:
                if resource[mapping] in self.configraw[ctype]:
                    resource[mapping] = self.configraw[ctype][resource[mapping]]

    def multiple_relation(self, resource, mapping, ctype):
        """
        Convert multiple embedded data to name of relation_data
        Example:
        {'contacts': [{'_id': a3659204fe,'contact_name':'admin'},
                      {'_id': a3659204ff,'contact_name':'admin2'}]}
        converted to:
        {'contacts': 'admin,admin2'}

        :param resource: dictionary got from alignak-backend
        :type resource: dict
        :param mapping: key value of resource
        :type mapping: str
        :param ctype: type of configraw (hosts, services, commands...)
        :type ctype: str
        """
        if mapping in resource:
            members = []
            for member in resource[mapping]:
                if member in self.configraw[ctype]:
                    members.append(self.configraw[ctype][member])
            resource[mapping] = ','.join(members)

    @classmethod
    def clean_unusable_keys(cls, resource):
        """
        Delete keys of dictionary not used

        :param resource: dictionary got from alignak-backend
        :type resource: dict
        :return:
        """
        fields = ['_links', '_updated', '_created', '_etag', '_id', 'name', 'ui']
        for field in fields:
            if field in resource:
                del resource[field]

    @classmethod
    def convert_lists(cls, resource):
        """
        Convert lists into string with values separated with comma

        :param resource: ressource
        :type resource: dict
        :return: None
        """
        for prop in resource:
            if isinstance(resource[prop], list):
                resource[prop] = ','.join(str(e) for e in resource[prop])
            elif isinstance(resource[prop], dict):
                logger.warning("=====> %s", prop)
                logger.warning(resource[prop])

    def get_commands(self):
        """
        Get commands from alignak_backend

        :return: None
        """
        self.configraw['commands'] = {}
        all_commands = self.backend.get_all('command')
        logger.warning("[Alignak Backend Arbit] Got %d commands", len(all_commands))
        for command in all_commands:
            self.configraw['commands'][command['_id']] = command['name']
            command['imported_from'] = 'alignakbackend'
            command['command_name'] = command['name']
            self.clean_unusable_keys(command)
            self.convert_lists(command)
            self.config['commands'].append(command)

    def get_timeperiods(self):
        """
        Get timeperiods from alignak_backend

        :return: None
        """
        self.configraw['timeperiods'] = {}
        all_timeperiods = self.backend.get_all('timeperiod')
        for timeperiod in all_timeperiods:
            self.configraw['timeperiods'][timeperiod['_id']] = timeperiod['name']
            timeperiod['imported_from'] = 'alignakbackend'
            timeperiod['timeperiod_name'] = timeperiod['name']
            for daterange in timeperiod['dateranges']:
                timeperiod.update(daterange)
            del timeperiod['dateranges']
            self.clean_unusable_keys(timeperiod)
            self.convert_lists(timeperiod)
            self.config['timeperiods'].append(timeperiod)

    def get_contactgroups(self):
        """
        Get contactgroups from alignak_backend

        :return: None
        """
        self.configraw['contactgroups'] = {}
        all_contactgroups = self.backend.get_all('contactgroup')
        logger.warning("[Alignak Backend Arbit] Got %d contactgroups", len(all_contactgroups))
        for contactgroup in all_contactgroups:
            self.configraw['contactgroups'][contactgroup['_id']] = contactgroup['name']
            contactgroup['imported_from'] = 'alignakbackend'
            contactgroup['contactgroup_name'] = contactgroup['name']
            self.clean_unusable_keys(contactgroup)
            self.convert_lists(contactgroup)
            self.config['contactgroups'].append(contactgroup)

    def get_contact(self):
        """
        Get contacts from alignak_backend

        :return: None
        """
        self.configraw['contacts'] = {}
        all_contacts = self.backend.get_all('contact')
        for contact in all_contacts:
            self.configraw['contacts'][contact['_id']] = contact['name']
            contact['imported_from'] = 'alignakbackend'
            contact['contact_name'] = contact['name']

            # host_notification_period
            self.single_relation(contact, 'host_notification_period', 'timeperiods')
            # service_notification_period
            self.single_relation(contact, 'service_notification_period', 'timeperiods')
            # host_notification_commands
            self.multiple_relation(contact, 'host_notification_commands', 'commands')
            # service_notification_commands
            self.multiple_relation(contact, 'service_notification_commands', 'commands')
            # contactgroups
            self.multiple_relation(contact, 'contactgroups', 'contactgroups')

            if 'host_notification_commands' not in contact:
                contact['host_notification_commands'] = ''
            if 'service_notification_commands' not in contact:
                contact['service_notification_commands'] = ''
            if 'host_notification_period' not in contact:
                contact['host_notification_period'] = \
                    self.config['timeperiods'][0]['timeperiod_name']
                contact['host_notifications_enabled'] = False
            if 'service_notification_period' not in contact:
                contact['service_notification_period'] = \
                    self.config['timeperiods'][0]['timeperiod_name']
                contact['service_notifications_enabled'] = False
            self.clean_unusable_keys(contact)
            self.convert_lists(contact)
            self.config['contacts'].append(contact)

    def get_hostgroups(self):
        """
        Get hostgroups from alignak_backend

        :return: None
        """
        self.configraw['hostgroups'] = {}
        all_hostgroups = self.backend.get_all('hostgroup')
        logger.warning("[Alignak Backend Arbit] Got %d hostgroups", len(all_hostgroups))
        for hostgroup in all_hostgroups:
            self.configraw['hostgroups'][hostgroup['_id']] = hostgroup['name']
            hostgroup['imported_from'] = 'alignakbackend'
            hostgroup['hostgroup_name'] = hostgroup['name']
            # members
            # ## self.multiple_relation(hostgroup, 'members', 'host_name')
            hostgroup['members'] = ''
            # hostgroup_members
            # ## self.multiple_relation(hostgroup, 'hostgroup_members', 'hostgroup_name')
            hostgroup['hostgroup_members'] = ''
            # realm
            if hostgroup['realm'] is None:
                del hostgroup['realm']

            self.clean_unusable_keys(hostgroup)
            self.convert_lists(hostgroup)
            self.config['hostgroups'].append(hostgroup)

    def get_hosts(self):
        """
        Get hosts from alignak_backend

        :return: None
        """
        self.configraw['hosts'] = {}
        all_hosts = self.backend.get_all('host')
        logger.warning("[Alignak Backend Arbit] Got %d hosts", len(all_hosts))
        for host in all_hosts:
            self.configraw['hosts'][host['_id']] = host['name']
            host['host_name'] = host['name']
            host['imported_from'] = 'alignakbackend'
            # check_command
            if 'check_command' in host:
                if host['check_command'] is None:
                    host['check_command'] = ''
                elif host['check_command'] in self.configraw['commands']:
                    host['check_command'] = self.configraw['commands'][host['check_command']]
                else:
                    host['check_command'] = ''
            if 'check_command_args' in host:
                if 'check_command' not in host:
                    host['check_command'] = ''
                elif host['check_command_args'] != '':
                    host['check_command'] += '!'
                    host['check_command'] += host['check_command_args']
                del host['check_command_args']
            # check_period
            self.single_relation(host, 'check_period', 'timeperiods')
            # notification_period
            self.single_relation(host, 'notification_period', 'timeperiods')
            # parents
            # ## self.multiple_relation(host, 'parents', 'host_name')
            host['parents'] = ''
            # hostgroups
            self.multiple_relation(host, 'hostgroups', 'hostgroups')
            # contacts
            self.multiple_relation(host, 'contacts', 'contacts')
            # contact_groups
            self.multiple_relation(host, 'contact_groups', 'contactgroups')
            # escalations
            # ## self.multiple_relation(host, 'escalations', 'escalation_name')
            if 'escalation' in host and host['escalation'] == '':
                del host['escalation']
            if 'alias' in host and host['alias'] == '':
                del host['alias']
            if 'realm' in host:
                if host['realm'] is None:
                    del host['realm']
            self.clean_unusable_keys(host)
            self.convert_lists(host)
            self.config['hosts'].append(host)

    def get_servicegroups(self):
        """
        Get servicegroups from alignak_backend

        :return: None
        """
        self.configraw['servicegroups'] = {}
        all_servicegroups = self.backend.get_all('servicegroup')
        logger.warning("[Alignak Backend Arbit] Got %d servicegroups", len(all_servicegroups))
        for servicegroup in all_servicegroups:
            self.configraw['servicegroups'][servicegroup['_id']] = servicegroup['name']
            servicegroup['imported_from'] = 'alignakbackend'
            servicegroup['servicegroup_name'] = servicegroup['name']
            # members
            # ## self.multiple_relation(servicegroup, 'members', 'service_description')
            servicegroup['members'] = ''
            # servicegroup_members
            # ## self.multiple_relation(servicegroup, 'servicegroup_members', 'servicegroup_name')
            servicegroup['servicegroup_members'] = ''
            # realm
            if servicegroup['realm'] is None:
                del servicegroup['realm']

            self.clean_unusable_keys(servicegroup)
            self.convert_lists(servicegroup)
            self.config['servicegroups'].append(servicegroup)

    def get_services(self):
        """
        Get services from alignak_backend

        :return: None
        """
        params = {'embedded': '{"escalations":1,"service_dependencies":1}'}
        all_services = self.backend.get_all('service', params)
        logger.warning("[Alignak Backend Arbit] Got %d services", len(all_services))
        for service in all_services:
            service['imported_from'] = 'alignakbackend'
            service['service_description'] = service['name']
            # check_command
            if 'check_command' in service:
                if service['check_command'] is None:
                    del service['check_command']
                elif service['check_command'] in self.configraw['commands']:
                    service['check_command'] = self.configraw['commands'][service['check_command']]
                else:
                    del service['check_command']
            if 'check_command_args' in service:
                if 'check_command' not in service:
                    service['check_command'] = ''
                else:
                    service['check_command'] += '!'
                service['check_command'] += service['check_command_args']
                del service['check_command_args']
            # host_name
            self.single_relation(service, 'host_name', 'hosts')
            # check_period
            self.single_relation(service, 'check_period', 'timeperiods')
            # notification_period
            self.single_relation(service, 'notification_period', 'timeperiods')
            # maintenance_period
            self.single_relation(service, 'maintenance_period', 'timeperiods')
            # servicegroups
            self.multiple_relation(service, 'servicegroups', 'servicegroups')
            # contacts
            self.multiple_relation(service, 'contacts', 'contacts')
            # contact_groups
            self.multiple_relation(service, 'contact_groups', 'contactgroups')
            # escalations
            # ## self.multiple_relation(service, 'escalations', 'escalation_name')
            if 'escalation' in service and service['escalation'] == '':
                del service['escalation']
            # service_dependencies
            # ## self.multiple_relation(service, 'service_dependencies', 'service_name')
            service['service_dependencies'] = ''
            if 'alias' in service and service['alias'] == '':
                del service['alias']

            self.clean_unusable_keys(service)
            self.convert_lists(service)
            self.config['services'].append(service)

    def get_objects(self):
        """
        Get objects from alignak-backend

        :return: configuration objects
        :rtype: dict
        """
        start_time = time.time()
        self.get_commands()
        self.get_timeperiods()
        self.get_contactgroups()
        self.get_contact()
        self.get_hostgroups()
        self.get_hosts()
        self.get_servicegroups()
        self.get_services()
        logger.info("[backend arbiter] loaded in --- %s seconds ---", (time.time() - start_time))

        return self.config