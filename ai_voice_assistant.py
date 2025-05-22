
def handle_voice_command(command_text):
    if "show dashboard" in command_text.lower():
        return "Loading facility dashboard..."
    elif "generate report" in command_text.lower():
        return "Compiling board packet..."
    else:
        return "Sorry, I didn't understand that request."
