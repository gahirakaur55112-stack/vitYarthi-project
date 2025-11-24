import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
        
    response('Hello!', ['hello', 'hi', 'hey', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)

    response(long.R_LOCATION, ['where', 'is','vitb','located','vit','bhopal'], required_words=['located'])
    response(long.R_FEES, ['who', 'should', 'i','contact','for','fees','related','problems'], required_words=['fees','problems'])
    response(long.R_CTS, ['what', 'is', 'the','contact','information','of','cts'], required_words=['cts'])
    response(long.R_LADIES_HOSTEL, ['what', 'is', 'the','contact','information','of','ladies','hostel','chief','warden'], required_words=['ladies','chief'])
    response(long.R_BOYS_HOSTEL, ['what', 'is', 'the','contact','information','of','boys','hostel','chief','warden'], required_words=['boys','chief'])
    response(long.R_ADMISSION, ['how','can','i','get','admission','in','vitb','vit','bhopal'], required_words=['admission'])
    response(long.R_PLACEMENTS, ['what', 'are','the','placements','statistics','of','vitb','vit','bhopal'], required_words=['placements'])
    response(long.R_CHANCELLOR, ['who','is','the','chancellor','of','vitb','vit','bhopal'], required_words=['chancellor'])
    response(long.R_AGE, ['how','old','is','vitb','vit','bhopal'], required_words=['old'])

    
    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


while True:
    print('Bot: ' + get_response(input('You: ')))
    
