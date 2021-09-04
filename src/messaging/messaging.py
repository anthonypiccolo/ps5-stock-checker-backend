
import discord_bot


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
        },
        "ebgames": {
            "disc": None,
            "digital": None
        }
    }


def create_messages_from_dict(input_dict):
    """
    extract only the relevant content from the base dictionary
    then put it into a string we can post to message channels with a 
    """
    messages = []
    for key in input_dict:
        for sku in ["disc","digital"]:
            if input_dict[key][sku] != None:
                messages.append(f"PS5 {sku} found at {key}: {input_dict[key][sku]}")
    return messages

def message_services(input_dict):
    """ the messaging entity which will handle all the federation of messages 
    should be instantiated with the standard json body and this class will handle the extraction
    and messaging
    """

    messages = create_messages_from_dict(input_dict)

    if len(messages)>0:
        for each_message in messages:
            discord_bot.notify_discord(each_message)
            #slack thing here
            #email here




