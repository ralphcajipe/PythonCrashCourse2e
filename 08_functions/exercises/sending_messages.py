# Sending Messages

def send_messages(unsent_messages, sent_messages):
    """
    Simulate printing each text message and
    move each message to a new list called sent_messages.
    """
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


def show_messages(sent_messages):
    """Show all messages that were sent."""
    print("\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)


unsent_messages = ["I'll be there", 'Running late', 'At the lobby']
sent_messages = []

send_messages(unsent_messages, sent_messages)
show_messages(sent_messages)

print("\nStatus of lists:")
print(f"- unsent_messages -> {unsent_messages}")
print(f"- sent_messages -> {sent_messages}")
