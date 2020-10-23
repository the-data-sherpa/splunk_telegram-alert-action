
# encoding = utf-8
# Always put this line at the beginning of this file
import alert_telegram_declare

import os
import sys

from alert_actions_base import ModularAlertBase
import modalert_telegram_helper

class AlertActionWorkertelegram(ModularAlertBase):

    def __init__(self, ta_name, alert_name):
        super(AlertActionWorkertelegram, self).__init__(ta_name, alert_name)

    def validate_params(self):

        if not self.get_param("event_title"):
            self.log_error('event_title is a mandatory parameter, but its value is None.')
            return False

        if not self.get_param("message"):
            self.log_error('message is a mandatory parameter, but its value is None.')
            return False

        if not self.get_param("severity"):
            self.log_error('severity is a mandatory parameter, but its value is None.')
            return False

        if not self.get_param("bot_id"):
            self.log_error('bot_id is a mandatory parameter, but its value is None.')
            return False

        if not self.get_param("chat_id"):
            self.log_error('chat_id is a mandatory parameter, but its value is None.')
            return False
        return True

    def process_event(self, *args, **kwargs):
        status = 0
        try:
            if not self.validate_params():
                return 3
            status = modalert_telegram_helper.process_event(self, *args, **kwargs)
        except (AttributeError, TypeError) as ae:
            self.log_error("Error: {}. Please double check spelling and also verify that a compatible version of Splunk_SA_CIM is installed.".format(str(ae)))
            return 4
        except Exception as e:
            msg = "Unexpected error: {}."
            if e:
                self.log_error(msg.format(str(e)))
            else:
                import traceback
                self.log_error(msg.format(traceback.format_exc()))
            return 5
        return status

if __name__ == "__main__":
    exitcode = AlertActionWorkertelegram("alert_telegram", "telegram").run(sys.argv)
    sys.exit(exitcode)
