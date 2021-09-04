
import discord_bot
import throttle
import time

example_payload = {
        "target": {
            "disc": "https://google.com",
            "digital": None
        },
        "bigw": {
            "disc": None,
            "digital": None
        },
        "amazon": {
            "disc": None,
            "digital": None
        }
        # ,
        # "ebgames": {
        #     "disc": None,
        #     "digital": None
        # }
    }


def create_messages_from_dict(input_dict):
    """
    extract only the relevant content from the base dictionary
    then put it into a string we can post to message channels with a 
    """
    messages = []
    for key in input_dict:
        if key != "timestamp":  #ignore the data for timestamp on the payload
            for sku in ["disc","digital"]:
                if input_dict[key][sku] != None and input_dict[key][sku] != "":
                    messages.append(f"PS5 {sku} found at {key}: {input_dict[key][sku]}")
    return messages

def message_services(input_dict):
    """ the messaging entity which will handle all the federation of messages 
    should be instantiated with the standard json body and this class will handle the extraction
    and messaging
    """

    #check throttle here
    throttled_dict = throttle.throttle_dict(input_dict)
    print("throttled_dict")
    print(throttled_dict)
    messages = create_messages_from_dict(throttled_dict) #only message data which is let through the throttle

    if len(messages)>0:
        print(f"sending {len(messages)} messages")
        output_message = '\n'.join(messages)
        discord_bot.notify_discord(output_message)
        # for each_message in messages:
        #     discord_bot.notify_discord(each_message)
        #     #slack thing here
        #     #email here
    else:
        print("no messages to send.")



# message_services(example_payload)   # use this to deliver to all messaing services we have
