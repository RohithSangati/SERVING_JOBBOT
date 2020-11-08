def get_intent(message):
    m=message.lower()               #Converting user input to lower case for ease of use
    if any(x in m for x in ['trending','technologies','trending technologies','top technologies']):
        return 'trending technologies'          
    elif any(x in m for x in ['interview','tips','interview tips']):
        return 'interview tips'
    elif any(x in m for x in ['job','requirements','current']):
        return 'job requirements'
    elif any(x in m for x in ['tutorials','online tutorials','courses','platforms','online']):
        return 'online platforms'
    elif any(x in m for x in ['end','bye']):
        return 'end'
    else:
        return 'invalid'

def handle(data):
    from flask import render_template
    intent=get_intent(data['message'])
    if intent=='trending technologies':                                               
        return render_template('messages/trending.html',data=data)
    elif intent=='job requirements':
        return render_template('messages/jobrequirements.html',data=data)
    elif intent=='interview tips':
        return render_template('messages/tips.html',data=data)
    elif intent=='online platforms':
        return render_template('messages/platforms.html',data=data)
    elif intent=='end':
        return render_template('messages/final.html',data=data)
    else:
        return render_template('messages/invalid.html',data=data)