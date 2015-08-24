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

from httmock import all_requests, response, HTTMock
import ujson
import unittest2
from alignak.modules.mod_alignakbackendsched.module import AlignakBackendSched
from alignak.objects.module import Module


@all_requests
def response_get_all_hosts(url, request):
    headers = {'content-type': 'application/json'}
    content = '{}'
    if request.method == 'GET':
        if url.path == '/host':
            if url.query == 'projection=%7B%22host_name%22:1%7D':
                content = '{"_items": [{"_updated": "Thu, 01 Jan 1970 00:00:00 GMT", "_links": {"self": {"href": "host/55d4a5246376e946db235fbc", "title": "Host"}}, "host_name": "server1", "_created": "Thu, 01 Jan 1970 00:00:00 GMT", "_id": "55d4a5246376e946db235fbc", "_etag": "3e7dcc08e17493205d117a0ef36e452f59cd5d0f"}, {"_updated": "Thu, 01 Jan 1970 00:00:00 GMT", "_links": {"self": {"href": "host/55d4a5276376e946db235fbd", "title": "Host"}}, "host_name": "server2", "_created": "Thu, 01 Jan 1970 00:00:00 GMT", "_id": "55d4a5276376e946db235fbd", "_etag": "c26a81d0f6ce066938a66a1252c31d64eb97d836"}, {"_updated": "Thu, 01 Jan 1970 00:00:00 GMT", "_links": {"self": {"href": "host/55d4a52a6376e946db235fbe", "title": "Host"}}, "host_name": "server3", "_created": "Thu, 01 Jan 1970 00:00:00 GMT", "_id": "55d4a52a6376e946db235fbe", "_etag": "56321ee365616dde0a37c2e2449c771495da8362"}, {"_updated": "Thu, 01 Jan 1970 00:00:00 GMT", "_links": {"self": {"href": "host/55d4a52d6376e946db235fbf", "title": "Host"}}, "host_name": "server4", "_created": "Thu, 01 Jan 1970 00:00:00 GMT", "_id": "55d4a52d6376e946db235fbf", "_etag": "4ef62d3fb11f487f8437f753b314324be9ccdffc"}], "_links": {"self": {"href": "host", "title": "host"}, "parent": {"href": "/", "title": "home"}}, "_meta": {"max_results": 25, "total": 4, "page": 1}}'
        elif url.path == '/livehost':
            if url.query == 'embedded=%7B%22host_name%22:1%7D&projection=%7B%22host_name%22:1%7D':
                content = '{"_items": [{"_updated": "Wed, 19 Aug 2015 20:21:54 GMT", "_links": {"self": {"href": "livehost/55d4e5626376e946db235fc0", "title": "Livehost"}}, "host_name": {"active_checks_enabled": true, "business_impact_modulations": [], "retry_interval": 0, "service_includes": [], "reactionner_tag": "None", "escalations": [], "retain_status_information": true, "low_flap_threshold": 50, "process_perf_data": true, "service_overrides": [], "snapshot_interval": 5, "notification_interval": 60, "trending_policies": [], "failure_prediction_enabled": false, "flap_detection_options": ["o", "d", "u"], "resultmodulations": [], "snapshot_enabled": false, "business_rule_downtime_as_ack": false, "stalking_options": [], "event_handler_enabled": false, "snapshot_criteria": ["d", "u"], "initial_state": "u", "first_notification_delay": 0, "flap_detection_enabled": true, "notification_options": ["d", "u", "r", "f"], "host_name": "server1", "labels": [], "definition_order": 100, "macromodulations": [], "retain_nonstatus_information": true, "notifications_enabled": true, "business_rule_smart_notifications": false, "obsess_over_host": false, "freshness_threshold": 0, "service_excludes": [], "imported_from": "unknown", "business_rule_host_notification_options": [], "_updated": "Wed, 19 Aug 2015 15:47:48 GMT", "time_to_orphanage": 300, "trigger_broker_raise_enabled": false, "custom_views": [], "register": true, "checkmodulations": [], "poller_tag": "None", "passive_checks_enabled": true, "check_interval": 0, "business_impact": 2, "_created": "Wed, 19 Aug 2015 15:47:48 GMT", "max_check_attempts": 1, "_id": "55d4a5246376e946db235fbc", "_etag": "6bcd6c6fcc4e849377d1390d9ad161474a4212a9", "business_rule_service_notification_options": [], "check_freshness": false}, "_created": "Wed, 19 Aug 2015 20:21:54 GMT", "_id": "55d4e5626376e946db235fc0", "_etag": "78462b947415c0703d5bb747e8bc1fdb0e088a3b"}, {"_updated": "Wed, 19 Aug 2015 20:22:21 GMT", "_links": {"self": {"href": "livehost/55d4e57d6376e946db235fc1", "title": "Livehost"}}, "host_name": {"active_checks_enabled": true, "business_impact_modulations": [], "retry_interval": 0, "service_includes": [], "reactionner_tag": "None", "escalations": [], "retain_status_information": true, "low_flap_threshold": 50, "process_perf_data": true, "service_overrides": [], "snapshot_interval": 5, "notification_interval": 60, "trending_policies": [], "failure_prediction_enabled": false, "flap_detection_options": ["o", "d", "u"], "resultmodulations": [], "snapshot_enabled": false, "business_rule_downtime_as_ack": false, "stalking_options": [], "event_handler_enabled": false, "snapshot_criteria": ["d", "u"], "initial_state": "u", "first_notification_delay": 0, "flap_detection_enabled": true, "notification_options": ["d", "u", "r", "f"], "host_name": "server2", "labels": [], "definition_order": 100, "macromodulations": [], "retain_nonstatus_information": true, "notifications_enabled": true, "business_rule_smart_notifications": false, "obsess_over_host": false, "freshness_threshold": 0, "service_excludes": [], "imported_from": "unknown", "business_rule_host_notification_options": [], "_updated": "Wed, 19 Aug 2015 15:47:51 GMT", "time_to_orphanage": 300, "trigger_broker_raise_enabled": false, "custom_views": [], "register": true, "checkmodulations": [], "poller_tag": "None", "passive_checks_enabled": true, "check_interval": 0, "business_impact": 2, "_created": "Wed, 19 Aug 2015 15:47:51 GMT", "max_check_attempts": 1, "_id": "55d4a5276376e946db235fbd", "_etag": "033a2082ff086da9825c30baed8f106b6cdac694", "business_rule_service_notification_options": [], "check_freshness": false}, "_created": "Wed, 19 Aug 2015 20:22:21 GMT", "_id": "55d4e57d6376e946db235fc1", "_etag": "3524b87876c1d457bdca7492b9bfc503f3f13b1e"}], "_links": {"self": {"href": "livehost", "title": "livehost"}, "parent": {"href": "/", "title": "home"}}, "_meta": {"max_results": 25, "total": 2, "page": 1}}'
        if url.path == '/service':
            if url.query == 'projection=%7B%22service_description%22:1,%22host_name%22:1%7D&embedded=%7B%22host_name%22:1%7D':
                content = '{"_items": [{"_updated": "Thu, 01 Jan 1970 00:00:00 GMT", "_links": {"self": {"href": "service/55d4f7b26376e946db235fc4", "title": "Service"}}, "host_name": {"active_checks_enabled": true, "business_impact_modulations": [], "retry_interval": 0, "service_includes": [], "reactionner_tag": "None", "escalations": [], "retain_status_information": true, "low_flap_threshold": 50, "process_perf_data": true, "service_overrides": [], "snapshot_interval": 5, "notification_interval": 60, "trending_policies": [], "failure_prediction_enabled": false, "flap_detection_options": ["o", "d", "u"], "resultmodulations": [], "snapshot_enabled": false, "business_rule_downtime_as_ack": false, "stalking_options": [], "event_handler_enabled": false, "snapshot_criteria": ["d", "u"], "initial_state": "u", "first_notification_delay": 0, "flap_detection_enabled": true, "notification_options": ["d", "u", "r", "f"], "host_name": "server1", "labels": [], "definition_order": 100, "macromodulations": [], "retain_nonstatus_information": true, "notifications_enabled": true, "business_rule_smart_notifications": false, "obsess_over_host": false, "freshness_threshold": 0, "service_excludes": [], "imported_from": "unknown", "business_rule_host_notification_options": [], "_updated": "Wed, 19 Aug 2015 15:47:48 GMT", "time_to_orphanage": 300, "trigger_broker_raise_enabled": false, "custom_views": [], "register": true, "checkmodulations": [], "poller_tag": "None", "passive_checks_enabled": true, "check_interval": 0, "business_impact": 2, "_created": "Wed, 19 Aug 2015 15:47:48 GMT", "max_check_attempts": 1, "_id": "55d4a5246376e946db235fbc", "_etag": "6bcd6c6fcc4e849377d1390d9ad161474a4212a9", "business_rule_service_notification_options": [], "check_freshness": false}, "_created": "Thu, 01 Jan 1970 00:00:00 GMT", "service_description": "check disk", "_id": "55d4f7b26376e946db235fc4", "_etag": "1943f4e75be5e80da66a9c93826029936001734f"}, {"_updated": "Thu, 01 Jan 1970 00:00:00 GMT", "_links": {"self": {"href": "service/55d4f7be6376e946db235fc5", "title": "Service"}}, "host_name": {"active_checks_enabled": true, "business_impact_modulations": [], "retry_interval": 0, "service_includes": [], "reactionner_tag": "None", "escalations": [], "retain_status_information": true, "low_flap_threshold": 50, "process_perf_data": true, "service_overrides": [], "snapshot_interval": 5, "notification_interval": 60, "trending_policies": [], "failure_prediction_enabled": false, "flap_detection_options": ["o", "d", "u"], "resultmodulations": [], "snapshot_enabled": false, "business_rule_downtime_as_ack": false, "stalking_options": [], "event_handler_enabled": false, "snapshot_criteria": ["d", "u"], "initial_state": "u", "first_notification_delay": 0, "flap_detection_enabled": true, "notification_options": ["d", "u", "r", "f"], "host_name": "server2", "labels": [], "definition_order": 100, "macromodulations": [], "retain_nonstatus_information": true, "notifications_enabled": true, "business_rule_smart_notifications": false, "obsess_over_host": false, "freshness_threshold": 0, "service_excludes": [], "imported_from": "unknown", "business_rule_host_notification_options": [], "_updated": "Wed, 19 Aug 2015 15:47:51 GMT", "time_to_orphanage": 300, "trigger_broker_raise_enabled": false, "custom_views": [], "register": true, "checkmodulations": [], "poller_tag": "None", "passive_checks_enabled": true, "check_interval": 0, "business_impact": 2, "_created": "Wed, 19 Aug 2015 15:47:51 GMT", "max_check_attempts": 1, "_id": "55d4a5276376e946db235fbd", "_etag": "033a2082ff086da9825c30baed8f106b6cdac694", "business_rule_service_notification_options": [], "check_freshness": false}, "_created": "Thu, 01 Jan 1970 00:00:00 GMT", "service_description": "check disk", "_id": "55d4f7be6376e946db235fc5", "_etag": "82d8aa840db96bb124e015935b39ab584e2cb64d"}, {"_updated": "Thu, 01 Jan 1970 00:00:00 GMT", "_links": {"self": {"href": "service/55d4f7cc6376e946db235fc6", "title": "Service"}}, "host_name": {"active_checks_enabled": true, "business_impact_modulations": [], "retry_interval": 0, "service_includes": [], "reactionner_tag": "None", "escalations": [], "retain_status_information": true, "low_flap_threshold": 50, "process_perf_data": true, "service_overrides": [], "snapshot_interval": 5, "notification_interval": 60, "trending_policies": [], "failure_prediction_enabled": false, "flap_detection_options": ["o", "d", "u"], "resultmodulations": [], "snapshot_enabled": false, "business_rule_downtime_as_ack": false, "stalking_options": [], "event_handler_enabled": false, "snapshot_criteria": ["d", "u"], "initial_state": "u", "first_notification_delay": 0, "flap_detection_enabled": true, "notification_options": ["d", "u", "r", "f"], "host_name": "server3", "labels": [], "definition_order": 100, "macromodulations": [], "retain_nonstatus_information": true, "notifications_enabled": true, "business_rule_smart_notifications": false, "obsess_over_host": false, "freshness_threshold": 0, "service_excludes": [], "imported_from": "unknown", "business_rule_host_notification_options": [], "_updated": "Wed, 19 Aug 2015 15:47:54 GMT", "time_to_orphanage": 300, "trigger_broker_raise_enabled": false, "custom_views": [], "register": true, "checkmodulations": [], "poller_tag": "None", "passive_checks_enabled": true, "check_interval": 0, "business_impact": 2, "_created": "Wed, 19 Aug 2015 15:47:54 GMT", "max_check_attempts": 1, "_id": "55d4a52a6376e946db235fbe", "_etag": "06a762b9a4e1a60c7b5ed92c2fbd874c6ca75a65", "business_rule_service_notification_options": [], "check_freshness": false}, "_created": "Thu, 01 Jan 1970 00:00:00 GMT", "service_description": "check disk", "_id": "55d4f7cc6376e946db235fc6", "_etag": "8c59d9d3024a1278335d0d98fe1d0fed887f92df"}, {"_updated": "Thu, 01 Jan 1970 00:00:00 GMT", "_links": {"self": {"href": "service/55d4f7d76376e946db235fc7", "title": "Service"}}, "host_name": {"active_checks_enabled": true, "business_impact_modulations": [], "retry_interval": 0, "service_includes": [], "reactionner_tag": "None", "escalations": [], "retain_status_information": true, "low_flap_threshold": 50, "process_perf_data": true, "service_overrides": [], "snapshot_interval": 5, "notification_interval": 60, "trending_policies": [], "failure_prediction_enabled": false, "flap_detection_options": ["o", "d", "u"], "resultmodulations": [], "snapshot_enabled": false, "business_rule_downtime_as_ack": false, "stalking_options": [], "event_handler_enabled": false, "snapshot_criteria": ["d", "u"], "initial_state": "u", "first_notification_delay": 0, "flap_detection_enabled": true, "notification_options": ["d", "u", "r", "f"], "host_name": "server4", "labels": [], "definition_order": 100, "macromodulations": [], "retain_nonstatus_information": true, "notifications_enabled": true, "business_rule_smart_notifications": false, "obsess_over_host": false, "freshness_threshold": 0, "service_excludes": [], "imported_from": "unknown", "business_rule_host_notification_options": [], "_updated": "Wed, 19 Aug 2015 15:47:57 GMT", "time_to_orphanage": 300, "trigger_broker_raise_enabled": false, "custom_views": [], "register": true, "checkmodulations": [], "poller_tag": "None", "passive_checks_enabled": true, "check_interval": 0, "business_impact": 2, "_created": "Wed, 19 Aug 2015 15:47:57 GMT", "max_check_attempts": 1, "_id": "55d4a52d6376e946db235fbf", "_etag": "9d95fad66f44ced5dd65d70e6a68014e76def0f6", "business_rule_service_notification_options": [], "check_freshness": false}, "_created": "Thu, 01 Jan 1970 00:00:00 GMT", "service_description": "check disk", "_id": "55d4f7d76376e946db235fc7", "_etag": "64296d7209aed0cf1b3a332d0a6e57cc7eadb634"}], "_links": {"self": {"href": "service", "title": "service"}, "parent": {"href": "/", "title": "home"}}, "_meta": {"max_results": 25, "total": 4, "page": 1}}'
        elif url.path == '/liveservice':
            if url.query == 'embedded=%7B%22service_description%22:1%7D&projection=%7B%22service_description%22:1%7D':
                content = '{"_items": [{"_updated": "Wed, 19 Aug 2015 21:43:16 GMT", "_links": {"self": {"href": "liveservice/55d4f8746376e946db235fc8", "title": "Liveservice"}}, "service_description": {"active_checks_enabled": true, "business_impact_modulations": [], "labels": [], "reactionner_tag": "None", "is_volatile": false, "retain_status_information": true, "low_flap_threshold": -1, "process_perf_data": true, "snapshot_interval": 5, "default_value": [], "notification_interval": 60, "poller_tag": "None", "trending_policies": [], "failure_prediction_enabled": false, "flap_detection_options": ["o", "w", "c", "u"], "resultmodulations": [], "snapshot_enabled": false, "business_rule_downtime_as_ack": false, "stalking_options": [], "event_handler_enabled": false, "host_dependency_enabled": true, "snapshot_criteria": ["w", "c", "u"], "host_name": "55d4a5246376e946db235fbc", "escalations": [], "initial_state": "o", "first_notification_delay": 0, "flap_detection_enabled": true, "notification_options": ["w", "u", "c", "r", "f", "s"], "high_flap_threshold": -1, "definition_order": 100, "macromodulations": [], "retain_nonstatus_information": true, "notifications_enabled": true, "business_rule_host_notification_options": [], "aggregation": "", "business_rule_smart_notifications": false, "business_impact": 2, "freshness_threshold": 0, "service_description": "check disk", "obsess_over_host": false, "imported_from": "unknown", "service_dependencies": [], "_updated": "Wed, 19 Aug 2015 21:40:02 GMT", "time_to_orphanage": 300, "trigger_broker_raise_enabled": false, "custom_views": [], "register": true, "checkmodulations": [], "parallelize_check": true, "servicegroups": [], "passive_checks_enabled": true, "check_interval": 0, "merge_host_contacts": false, "_created": "Wed, 19 Aug 2015 21:40:02 GMT", "max_check_attempts": 1, "_id": "55d4f7b26376e946db235fc4", "_etag": "de5f790bd495a1ce42f00630aee4f13f56501da6", "business_rule_service_notification_options": [], "check_freshness": false}, "_created": "Wed, 19 Aug 2015 21:43:16 GMT", "_id": "55d4f8746376e946db235fc8", "_etag": "fbf6c05750113eca669aece45198affb567ac550"}, {"_updated": "Wed, 19 Aug 2015 21:43:35 GMT", "_links": {"self": {"href": "liveservice/55d4f8876376e946db235fc9", "title": "Liveservice"}}, "service_description": {"active_checks_enabled": true, "business_impact_modulations": [], "labels": [], "reactionner_tag": "None", "is_volatile": false, "retain_status_information": true, "low_flap_threshold": -1, "process_perf_data": true, "snapshot_interval": 5, "default_value": [], "notification_interval": 60, "poller_tag": "None", "trending_policies": [], "failure_prediction_enabled": false, "flap_detection_options": ["o", "w", "c", "u"], "resultmodulations": [], "snapshot_enabled": false, "business_rule_downtime_as_ack": false, "stalking_options": [], "event_handler_enabled": false, "host_dependency_enabled": true, "snapshot_criteria": ["w", "c", "u"], "host_name": "55d4a5276376e946db235fbd", "escalations": [], "initial_state": "o", "first_notification_delay": 0, "flap_detection_enabled": true, "notification_options": ["w", "u", "c", "r", "f", "s"], "high_flap_threshold": -1, "definition_order": 100, "macromodulations": [], "retain_nonstatus_information": true, "notifications_enabled": true, "business_rule_host_notification_options": [], "aggregation": "", "business_rule_smart_notifications": false, "business_impact": 2, "freshness_threshold": 0, "service_description": "check disk", "obsess_over_host": false, "imported_from": "unknown", "service_dependencies": [], "_updated": "Wed, 19 Aug 2015 21:40:14 GMT", "time_to_orphanage": 300, "trigger_broker_raise_enabled": false, "custom_views": [], "register": true, "checkmodulations": [], "parallelize_check": true, "servicegroups": [], "passive_checks_enabled": true, "check_interval": 0, "merge_host_contacts": false, "_created": "Wed, 19 Aug 2015 21:40:14 GMT", "max_check_attempts": 1, "_id": "55d4f7be6376e946db235fc5", "_etag": "b53ba39ec989a7bcd634582289de847797e04f67", "business_rule_service_notification_options": [], "check_freshness": false}, "_created": "Wed, 19 Aug 2015 21:43:35 GMT", "_id": "55d4f8876376e946db235fc9", "_etag": "3ed23c329f07c92fabeee465e5c4e59bc5f575f0"}], "_links": {"self": {"href": "liveservice", "title": "liveservice"}, "parent": {"href": "/", "title": "home"}}, "_meta": {"max_results": 25, "total": 2, "page": 1}}'
    elif request.method == 'POST':
        body = ujson.loads(request.body)
        if 'host_name' in body:
            if body['host_name'] == '55d4a52a6376e946db235fbe':
                # 55d4a52a6376e946db235fbe is server3
                content = '{"_updated": "Wed, 19 Aug 2015 20:32:19 GMT", "_links": {"self": {"href": "livehost/55d4e7d36376e946db235fc2", "title": "Livehost"}}, "_created": "Wed, 19 Aug 2015 20:32:19 GMT", "_status": "OK", "_id": "55d4e7d36376e946db235fc2", "_etag": "a457e78fe0dc28c1b427d9b0696096fee73f4a29"}'
            elif body['host_name'] == '55d4a52d6376e946db235fbf':
                # 55d4a52d6376e946db235fbf is server4
                content = '{"_updated": "Wed, 19 Aug 2015 20:33:22 GMT", "_links": {"self": {"href": "livehost/55d4e8126376e946db235fc3", "title": "Livehost"}}, "_created": "Wed, 19 Aug 2015 20:33:22 GMT", "_status": "OK", "_id": "55d4e8126376e946db235fc3", "_etag": "2b45425c497d5593bad8ef5413c84e6a0d61cc41"}'
        if 'service_description' in body:
            if body['service_description'] == '55d4f7cc6376e946db235fc6':
                content = '{"_updated": "Wed, 19 Aug 2015 21:52:34 GMT", "_links": {"self": {"href": "liveservice/55d4faa26376e946db235fca", "title": "Liveservice"}}, "_created": "Wed, 19 Aug 2015 21:52:34 GMT", "_status": "OK", "_id": "55d4faa26376e946db235fca", "_etag": "b7c4a2563f7382ed86dac2dc975759e20be778fc"}'
            elif body['service_description'] == '55d4f7d76376e946db235fc7':
                content = '{"_updated": "Wed, 19 Aug 2015 21:53:01 GMT", "_links": {"self": {"href": "liveservice/55d4fabd6376e946db235fcb", "title": "Liveservice"}}, "_created": "Wed, 19 Aug 2015 21:53:01 GMT", "_status": "OK", "_id": "55d4fabd6376e946db235fcb", "_etag": "9ab70e496605b755836be976d676be17a4bc6fea"}'
    return response(200, content, headers, None, 5, request)



class TestLivestatesGetrefs(unittest2.TestCase):

    def test_get_refs_host(self):
        """
        Get all hosts

        :return: None
        """
        modconf = Module()
        modconf.module_name = "alignakbackend"
        module = AlignakBackendSched(modconf)

        with HTTMock(response_get_all_hosts):
            module.get_refs('livehost')

        ref = {
            '55d4a5246376e946db235fbc': {
                '_id': '55d4e5626376e946db235fc0',
                '_etag': '78462b947415c0703d5bb747e8bc1fdb0e088a3b'
            },
            '55d4a5276376e946db235fbd': {
                '_id': '55d4e57d6376e946db235fc1',
                '_etag': '3524b87876c1d457bdca7492b9bfc503f3f13b1e'
            },
            '55d4a52a6376e946db235fbe': {
                '_id': '55d4e7d36376e946db235fc2',
                '_etag': 'a457e78fe0dc28c1b427d9b0696096fee73f4a29'
            },
            '55d4a52d6376e946db235fbf': {
                '_id': '55d4e8126376e946db235fc3',
                '_etag': '2b45425c497d5593bad8ef5413c84e6a0d61cc41'
            }
        }

        self.assertEqual(module.ref_live['host'], ref)

        mapping_ref = {
            'server1': '55d4a5246376e946db235fbc',
            'server2': '55d4a5276376e946db235fbd',
            'server3': '55d4a52a6376e946db235fbe',
            'server4': '55d4a52d6376e946db235fbf'
        }
        self.assertEqual(module.mapping['host'], mapping_ref)

    def test_get_refs_service(self):
        """
        Get all services

        :return: None
        """
        modconf = Module()
        modconf.module_name = "alignakbackend"
        module = AlignakBackendSched(modconf)

        with HTTMock(response_get_all_hosts):
            module.get_refs('liveservice')

        ref = {
            '55d4f7b26376e946db235fc4': {
                '_id': '55d4f8746376e946db235fc8',
                '_etag': 'fbf6c05750113eca669aece45198affb567ac550'
            },
            '55d4f7be6376e946db235fc5': {
                '_id': '55d4f8876376e946db235fc9',
                '_etag': '3ed23c329f07c92fabeee465e5c4e59bc5f575f0'
            },
            '55d4f7cc6376e946db235fc6': {
                '_id': '55d4faa26376e946db235fca',
                '_etag': 'b7c4a2563f7382ed86dac2dc975759e20be778fc'
            },
            '55d4f7d76376e946db235fc7': {
                '_id': '55d4fabd6376e946db235fcb',
                '_etag': '9ab70e496605b755836be976d676be17a4bc6fea'
            }
        }

        self.assertEqual(module.ref_live['service'], ref)

        mapping_ref = {
            'server1check disk': '55d4f7b26376e946db235fc4',
            'server2check disk': '55d4f7be6376e946db235fc5',
            'server3check disk': '55d4f7cc6376e946db235fc6',
            'server4check disk': '55d4f7d76376e946db235fc7'
        }
        self.assertEqual(module.mapping['service'], mapping_ref)
