# encoding = utf-8

def process_event(helper, *args, **kwargs):
    """
    # IMPORTANT
    # Do not remove the anchor macro:start and macro:end lines.
    # These lines are used to generate sample code. If they are
    # removed, the sample code will not be updated when configurations
    # are updated.

    [sample_code_macro:start]

    # The following example sends rest requests to some endpoint
    # response is a response object in python requests library
    response = helper.send_http_request("http://www.splunk.com", "GET", parameters=None,
                                        payload=None, headers=None, cookies=None, verify=True, cert=None, timeout=None, use_proxy=True)
    # get the response headers
    r_headers = response.headers
    # get the response body as text
    r_text = response.text
    # get response body as json. If the body text is not a json string, raise a ValueError
    r_json = response.json()
    # get response cookies
    r_cookies = response.cookies
    # get redirect history
    historical_responses = response.history
    # get response status code
    r_status = response.status_code
    # check the response status, if the status is not sucessful, raise requests.HTTPError
    response.raise_for_status()


    # The following example gets and sets the log level
    helper.set_log_level(helper.log_level)

    # The following example gets the alert action parameters and prints them to the log
    event_title = helper.get_param("event_title")
    helper.log_info("event_title={}".format(event_title))

    message = helper.get_param("message")
    helper.log_info("message={}".format(message))

    severity = helper.get_param("severity")
    helper.log_info("severity={}".format(severity))

    bot_id = helper.get_param("bot_id")
    helper.log_info("bot_id={}".format(bot_id))

    chat_id = helper.get_param("chat_id")
    helper.log_info("chat_id={}".format(chat_id))


    # The following example adds two sample events ("hello", "world")
    # and writes them to Splunk
    # NOTE: Call helper.writeevents() only once after all events
    # have been added
    helper.addevent("hello", sourcetype="sample_sourcetype")
    helper.addevent("world", sourcetype="sample_sourcetype")
    helper.writeevents(index="summary", host="localhost", source="localhost")

    # The following example gets the events that trigger the alert
    events = helper.get_events()
    for event in events:
        helper.log_info("event={}".format(event))

    # helper.settings is a dict that includes environment configuration
    # Example usage: helper.settings["server_uri"]
    helper.log_info("server_uri={}".format(helper.settings["server_uri"]))
    [sample_code_macro:end]
    """
    
    helper.log_info("Alert action telegram started.")
    
    search_name = helper.settings.get('search_name')
    event_title = helper.get_param("event_title")
    helper.log_info("event_title={}".format(event_title))
    message = helper.get_param("message")
    helper.log_info("message={}".format(message))
    severity = helper.get_param("severity")
    helper.log_info("severity={}".format(severity))
    chat_id = helper.get_param("chat_id")
    helper.log_info("chat_id={}".format(chat_id))
    bot_id = helper.get_param("bot_id")
    helper.log_info("bot_id={}".format(bot_id))
    search_name = helper.get_param("search_name")
    helper.log_info("search_name={}".format(search_name))
    results_link = helper.settings.get('results_link')
    helper.log_info("results_link={}".format(results_link))
    
    url = 'https://api.telegram.org/bot' + bot_id + '/sendMessage'
    
    message = "<b>SPLUNK ALERT MESSAGE\n------------------------------</b>\n<b>Alert Name</b>: {0} \n<b>SEVERITY</b>: {1} \n<b>MESSAGE</b>: {2} \n<b>Results Link</b>: {3}".format(event_title, severity, message, results_link)
    helper.log_debug("message={}".format(message))
    data={'chat_id': chat_id, 'text': message, 'parse_mode': "HTML"}
    
    response = helper.send_http_request(url, "POST", parameters=data,
                                        payload=None, headers=None, cookies=None, verify=True, cert=None, timeout=None, use_proxy=True)

    # TODO: Implement your alert action logic here
    return 0
