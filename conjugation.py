# coding: utf-8

#  Spanish verbs conjugation library. Based on Pythoñol (http://pythonol.sourceforge.net)
#
#  This software is distributed  free-of-charge and open source 
#  under the terms of the Free Education Initiative License.
#  
#  You should have received a copy  of this license with your copy of    
#  this software. If you did not, you may get a copy of the          
#  license at: http://github.com/voldmar/conjugation/blob/master/LICENSE

from collections import defaultdict

irregular_verbs = {}
reverse_irregular_verbs = defaultdict(list)

# Irregular verbs forms loading
with open('irregular_verbs.txt') as verbs_file:
    for line in verbs_file:
        if ':' not in line:
            continue
        infinitive, forms = line.decode('utf-8').strip().split(':')
        form_dict = {}
        for form in forms.split(','):
            # For some reason irregular_verbs.txt contains two form of one verb
            # We should ignore second form
            values = form.split('|')
            if len(values) == 2:
                key, value = values
                form_dict[key] = value
        irregular_verbs[infinitive] = form_dict

# We need defaultdict with list here because some verbs have same forms in various tenses
for verb, forms in irregular_verbs.iteritems():
    for form in forms.values():
        reverse_irregular_verbs[form].append(verb)

verb_endings = [
    u'ar', u'er', u'ir',
    u'arse', u'erse', u'irse',
    u'ár', u'ér', u'ír',
    u'árse', u'érse', u'írse',
]

ir_endings = {
    u'1pre': u'o', u'2pre': u'es', u'3pre': u'e',
    u'4pre': u'imos', u'5pre': u'ís', u'6pre': u'en',
    u'1pas': u'í', u'2pas': u'iste', u'3pas': u'ió',
    u'4pas': u'imos', u'5pas': u'isteis', u'6pas': u'ieron',
    u'1fut': u'iré', u'2fut': u'irás', u'3fut': u'irá',
    u'4fut': u'iremos', u'5fut': u'iréis', u'6fut': u'irán',
    u'1cop': u'ía', u'2cop': u'ías', u'3cop': u'ía',
    u'4cop': u'íamos', u'5cop': u'íais', u'6cop': u'ían',
    u'1pos': u'iría', u'2pos': u'irías', u'3pos': u'iría',
    u'4pos': u'iríamos', u'5pos': u'iríais', u'6pos': u'irían',
    u'1pres': u'a', u'2pres': u'as', u'3pres': u'a',
    u'4pres': u'amos', u'5pres': u'áis', u'6pres': u'an',
    u'1pass': u'iera', u'2pass': u'ieras', u'3pass': u'iera',
    u'4pass': u'iéramos', u'5pass': u'ierais', u'6pass': u'ieran',
    u'1passb': u'iese', u'2passb': u'ieses', u'3passb': u'iese',
    u'4passb': u'iésemos', u'5passb': u'ieseis', u'6passb': u'iesen',
    u'1futs': u'iere', u'2futs': u'ieres', u'3futs': u'iere',
    u'4futs': u'iéremos', u'5futs': u'iereis', u'6futs': u'ieren',
    u'1imp': '', u'2imp': u'e', u'3imp': u'a',
    u'4imp': u'amos', u'5imp': u'id', u'6imp': u'an',
    u'gerundio': u'iendo', u'participio': u'ido',
}

er_endings = {
    u'1pre': u'o', u'2pre': u'es', u'3pre': u'e',
    u'4pre': u'emos', u'5pre': u'éis', u'6pre': u'en',
    u'1pas': u'í', u'2pas': u'iste', u'3pas': u'ió',
    u'4pas': u'imos', u'5pas': u'isteis', u'6pas': u'ieron',
    u'1fut': u'eré', u'2fut': u'erás', u'3fut': u'erá',
    u'4fut': u'eremos', u'5fut': u'eréis', u'6fut': u'erán',
    u'1cop': u'ía', u'2cop': u'ías', u'3cop': u'ía',
    u'4cop': u'íamos', u'5cop': u'íais', u'6cop': u'ían',
    u'1pos': u'ería', u'2pos': u'erías', u'3pos': u'ería',
    u'4pos': u'eríamos', u'5pos': u'eríais', u'6pos': u'erían',
    u'1pres': u'a', u'2pres': u'as', u'3pres': u'a',
    u'4pres': u'amos', u'5pres': u'áis', u'6pres': u'an',
    u'1pass': u'iera', u'2pass': u'ieras', u'3pass': u'iera',
    u'4pass': u'iéramos', u'5pass': u'ierais', u'6pass': u'ieran',
    u'1passb': u'iese', u'2passb': u'ieses', u'3passb': u'iese',
    u'4passb': u'iésemos', u'5passb': u'ieseis', u'6passb': u'iesen',
    u'1futs': u'iere', u'2futs': u'ieres', u'3futs': u'iere',
    u'4futs': u'iéremos', u'5futs': u'iereis', u'6futs': u'ieren',
    u'1imp': '', u'2imp': u'e', u'3imp': u'a',
    u'4imp': u'amos', u'5imp': u'ed', u'6imp': u'an',
    u'gerundio': u'iendo', u'participio': u'ido',
}


ar_endings = {
    u'1pre': u'o', u'2pre': u'as', u'3pre': u'a',
    u'4pre': u'amos', u'5pre': u'áis', u'6pre': u'an',
    u'1pas': u'é', u'2pas': u'aste', u'3pas': u'ó',
    u'4pas': u'amos', u'5pas': u'steis', u'6pas': u'aron',
    u'1fut': u'aré', u'2fut': u'arás', u'3fut': u'ará',
    u'4fut': u'aremos', u'5fut': u'aréis', u'6fut': u'arán',
    u'1cop': u'aba', u'2cop': u'abas', u'3cop': u'aba',
    u'4cop': u'ábamos', u'5cop': u'abais', u'6cop': u'aban',
    u'1pos': u'aría', u'2pos': u'arías', u'3pos': u'aría',
    u'4pos': u'aríamos', u'5pos': u'aríais', u'6pos': u'arían',
    u'1pres': u'e', u'2pres': u'es', u'3pres': u'e',
    u'4pres': u'emos', u'5pres': u'éis', u'6pres': u'en',
    u'1pass': u'ara', u'2pass': u'aras', u'3pass': u'ara',
    u'4pass': u'áramos', u'5pass': u'arais', u'6pass': u'aran',
    u'1passb': u'ase', u'2passb': u'ases', u'3passb': u'ase',
    u'4passb': u'ásemos', u'5passb': u'aseis', u'6passb': u'asen',
    u'1futs': u'are', u'2futs': u'ares', u'3futs': u'are',
    u'4futs': u'áremos', u'5futs': u'areis', u'6futs': u'aren',
    u'1imp': '', u'2imp': u'a', u'3imp': u'e',
    u'4imp': u'emos', u'5imp': u'ad', u'6imp': u'en',
    u'gerundio': u'ando', u'participio': u'ado',
}

zar_endings = {
    u'1pas': u'cé',
    u'1pres': u'ce', u'2pres': u'ces', u'3pres': u'ce',
    u'4pres': u'cemos', u'5pres': u'céis', u'6pres': u'cen',
    u'3imp': u'ce', u'4imp': u'cemos', u'6imp': u'cen',
}

car_endings={
    u'1pas': u'qué',
    u'1pres': u'que', u'2pres': u'ques', u'3pres': u'que',
    u'4pres': u'quemos', u'5pres': u'quéis', u'6pres': u'quen',
    u'3imp': u'que', u'4imp': u'quemos', u'6imp': u'quen',
}

gar_endings={
    u'1pas': u'ué',
    u'1pres': u'ue', u'2pres': u'ues', u'3pres': u'ue',
    u'4pres': u'uemos', u'5pres': u'uéis', u'6pres': u'uen',
    u'3imp': u'ue', u'4imp': u'uemos', u'6imp': u'uen',
}

def is_verb(full_word):
    return any(full_word.endswith(ending) for ending in verb_endings)

def get_root(full_word):
    for ending in verb_endings:
        if full_word.endswith(ending):
            return full_word[:-len(ending)]
    raise ValueError(u'%s is not proper spanish verb' % full_word)

def get_base(full_word):
    return full_word[0:-2] if full_word.endswith(u'se') else full_word

def is_reflexive(full_word):
    return full_word.endswith(u'se')

def conjugate(full_word):
    full_word = full_word.lower().strip()
    print full_word
    if not is_verb(full_word):
        raise ValueError(u'%s is not proper spanish verb' % full_word)

    base = get_base(full_word)
    reflexive = is_reflexive(full_word)
    root = get_root(full_word)
    conjugations={}

    if base.endswith(u'ir') or base.endswith(u'ír'):
        conjugations.update((type, root + ending) for type, ending in ir_endings.items())

    if base.endswith(u'er') or base.endswith(u'ér'):
        conjugations.update((type, root + ending) for type, ending in er_endings.items())

    if base.endswith(u'ar') or base.endswith(u'ár'):
        conjugations.update((type, root + ending) for type, ending in ar_endings.items())
        if base.endswith(u'zar'):
            _root = root[:-1]
            conjugations.update((type, _root + ending) for type, ending in zar_endings.items())
        if base.endswith(u'gar'):
            conjugations.update((type, _root + ending) for type, ending in gar_endings.items())
        if base.endswith('car'):
            _root = root[:-1]
            conjugations.update((type, _root + ending) for type, ending in car_endings.items())

    if base in irregular_verbs:
        conjugations.update(irregular_verbs[base])

    if reflexive:
        for type, form in conjugations.items():
            if type.startswith(u'1'):
                conjugations[type] = u'me ' + conjugations[type]
            if type.startswith(u'2'):
                if type == u'2imp':
                    conjugations[type] = conjugations[type] + u'te' #exception for imperative
                else:
                    conjugations[type] = u'te ' + conjugations[type]
            if type.startswith(u'3'):
                if type == u'3imp':
                    conjugations[type] = conjugations[type] + u'se'
                else:
                    conjugations[type] = u'se ' + conjugations[type]
            if type.startswith(u'4'):
                if type == u'4imp':
                    conjugations[type] = conjugations[type] + u'nos'
                else:
                    conjugations[type] = u'nos ' + conjugations[type]
            if type.startswith(u'5'):
                if type == u'5imp':
                    conjugations[type] = conjugations[type] + u'os'
                else:
                    conjugations[type] = u'os ' + conjugations[type]
            if type.startswith(u'6'):
                if type == u'6imp':
                    conjugations[type] = conjugations[type] + u'se'
                else:
                    conjugations[type] = u'se ' + conjugations[type]

    conjugations.update(secondary_conjugations(base, reflexive))

    conjugations[u'1imp'] = u''
    conjugations[u'1impn'] = u''

    return conjugations

def secondary_conjugations(base, reflexive):
    conjugations = {}

    rdict = {u'1': '', u'2': '', u'3': '', u'4': '', u'5': '', u'6': ''}
    if reflexive:
        rdict = {
            u'1': u'me ', u'2': u'te ', u'3': u'se ',
            u'4': u'nos ', u'5': u'os ', u'6': u'se ',
        }

    conjugations[u'1fpop'] = rdict[u'1'] + u'voy a ' + base
    conjugations[u'2fpop'] = rdict[u'2'] + u'vas a ' + base
    conjugations[u'3fpop'] = rdict[u'3'] + u'va a ' + base
    conjugations[u'4fpop'] = rdict[u'4'] + u'vamos a ' + base
    conjugations[u'5fpop'] = rdict[u'5'] + u'vais a ' + base
    conjugations[u'6fpop'] = rdict[u'6'] + u'van a ' + base
    if conjugations.has_key(u'gerundio'):
        # present progressive
        conjugations[u'1ppro'] = rdict[u'1'] + u'estoy ' + conjugations[u'gerundio']
        conjugations[u'2ppro'] = rdict[u'2'] + u'estás ' + conjugations[u'gerundio']
        conjugations[u'3ppro'] = rdict[u'3'] + u'está ' + conjugations[u'gerundio']
        conjugations[u'4ppro'] = rdict[u'4'] + u'estamos ' + conjugations[u'gerundio']
        conjugations[u'5ppro'] = rdict[u'5'] + u'estáis ' + conjugations[u'gerundio']
        conjugations[u'6ppro'] = rdict[u'6'] + u'están ' + conjugations[u'gerundio']
        # future progressive
        conjugations[u'1fpro'] = rdict[u'1'] + u'estaré ' + conjugations[u'gerundio']
        conjugations[u'2fpro'] = rdict[u'2'] + u'estarás ' + conjugations[u'gerundio']
        conjugations[u'3fpro'] = rdict[u'3'] + u'estará ' + conjugations[u'gerundio']
        conjugations[u'4fpro'] = rdict[u'4'] + u'estaremos ' + conjugations[u'gerundio']
        conjugations[u'5fpro'] = rdict[u'5'] + u'estaréis ' + conjugations[u'gerundio']
        conjugations[u'6fpro'] = rdict[u'6'] + u'estarán ' + conjugations[u'gerundio']
        # future perfect progressive
        conjugations[u'1fpp'] = rdict[u'1'] + u'habré estado ' + conjugations[u'gerundio']
        conjugations[u'2fpp'] = rdict[u'2'] + u'habrás estado ' + conjugations[u'gerundio']
        conjugations[u'3fpp'] = rdict[u'3'] + u'habrá estado ' + conjugations[u'gerundio']
        conjugations[u'4fpp'] = rdict[u'4'] + u'habremos estado ' + conjugations[u'gerundio']
        conjugations[u'5fpp'] = rdict[u'5'] + u'habréis estado ' + conjugations[u'gerundio']
        conjugations[u'6fpp'] = rdict[u'6'] + u'habrán estado ' + conjugations[u'gerundio']
        # present perfect progressive
        conjugations[u'1ppp'] = rdict[u'1'] + u'he estado ' + conjugations[u'gerundio']
        conjugations[u'2ppp'] = rdict[u'2'] + u'has estado ' + conjugations[u'gerundio']
        conjugations[u'3ppp'] = rdict[u'3'] + u'ha estado ' + conjugations[u'gerundio']
        conjugations[u'4ppp'] = rdict[u'4'] + u'hemos estado ' + conjugations[u'gerundio']
        conjugations[u'5ppp'] = rdict[u'5'] + u'habéis estado ' + conjugations[u'gerundio']
        conjugations[u'6ppp'] = rdict[u'6'] + u'han estado ' + conjugations[u'gerundio']
        # conditional perfect progressive
        conjugations[u'1cpp'] = rdict[u'1'] + u'habría estado ' + conjugations[u'gerundio']
        conjugations[u'2cpp'] = rdict[u'2'] + u'habrías estado ' + conjugations[u'gerundio']
        conjugations[u'3cpp'] = rdict[u'3'] + u'habría estado ' + conjugations[u'gerundio']
        conjugations[u'4cpp'] = rdict[u'4'] + u'habríamos estado ' + conjugations[u'gerundio']
        conjugations[u'5cpp'] = rdict[u'5'] + u'habríais estado ' + conjugations[u'gerundio']
        conjugations[u'6cpp'] = rdict[u'6'] + u'habrían estado ' + conjugations[u'gerundio']
        # imperfect progressive
        conjugations[u'1ip'] = rdict[u'1'] + u'estaba ' + conjugations[u'gerundio']
        conjugations[u'2ip'] = rdict[u'2'] + u'estabas ' + conjugations[u'gerundio']
        conjugations[u'3ip'] = rdict[u'3'] + u'estaba ' + conjugations[u'gerundio']
        conjugations[u'4ip'] = rdict[u'4'] + u'estábamos ' + conjugations[u'gerundio']
        conjugations[u'5ip'] = rdict[u'5'] + u'estabais ' + conjugations[u'gerundio']
        conjugations[u'6ip'] = rdict[u'6'] + u'estaban ' + conjugations[u'gerundio']


    if conjugations.has_key(u'participio'):
        # present perfect
        conjugations[u'1pp'] = rdict[u'1'] + u'he ' + conjugations[u'participio']
        conjugations[u'2pp'] = rdict[u'2'] + u'has ' + conjugations[u'participio']
        conjugations[u'3pp'] = rdict[u'3'] + u'ha ' + conjugations[u'participio']
        conjugations[u'4pp'] = rdict[u'4'] + u'hemos ' + conjugations[u'participio']
        conjugations[u'5pp'] = rdict[u'5'] + u'habéis ' + conjugations[u'participio']
        conjugations[u'6pp'] = rdict[u'6'] + u'han ' + conjugations[u'participio']
        # past perfect
        conjugations[u'1pasp'] = rdict[u'1'] + u'había ' + conjugations[u'participio']
        conjugations[u'2pasp'] = rdict[u'2'] + u'habías ' + conjugations[u'participio']
        conjugations[u'3pasp'] = rdict[u'3'] + u'había ' + conjugations[u'participio']
        conjugations[u'4pasp'] = rdict[u'4'] + u'habíamos ' + conjugations[u'participio']
        conjugations[u'5pasp'] = rdict[u'5'] + u'habíais ' + conjugations[u'participio']
        conjugations[u'6pasp'] = rdict[u'6'] + u'habían ' + conjugations[u'participio']
        # preterit perfect
        conjugations[u'1prep'] = rdict[u'1'] + u'hube ' + conjugations[u'participio']
        conjugations[u'2prep'] = rdict[u'2'] + u'hubiste ' + conjugations[u'participio']
        conjugations[u'3prep'] = rdict[u'3'] + u'hubo ' + conjugations[u'participio']
        conjugations[u'4prep'] = rdict[u'4'] + u'hubimos ' + conjugations[u'participio']
        conjugations[u'5prep'] = rdict[u'5'] + u'hubisteis ' + conjugations[u'participio']
        conjugations[u'6prep'] = rdict[u'6'] + u'hubieron ' + conjugations[u'participio']
        # future perfect
        conjugations[u'1futp'] = rdict[u'1'] + u'habré ' + conjugations[u'participio']
        conjugations[u'2futp'] = rdict[u'2'] + u'habrás ' + conjugations[u'participio']
        conjugations[u'3futp'] = rdict[u'3'] + u'habrá ' + conjugations[u'participio']
        conjugations[u'4futp'] = rdict[u'4'] + u'habremos ' + conjugations[u'participio']
        conjugations[u'5futp'] = rdict[u'5'] + u'habréis ' + conjugations[u'participio']
        conjugations[u'6futp'] = rdict[u'6'] + u'habrán ' + conjugations[u'participio']
        # conditional perfect
        conjugations[u'1conp'] = rdict[u'1'] + u'habría ' + conjugations[u'participio']
        conjugations[u'2conp'] = rdict[u'2'] + u'habrías ' + conjugations[u'participio']
        conjugations[u'3conp'] = rdict[u'3'] + u'habría ' + conjugations[u'participio']
        conjugations[u'4conp'] = rdict[u'4'] + u'habríamos ' + conjugations[u'participio']
        conjugations[u'5conp'] = rdict[u'5'] + u'habríais ' + conjugations[u'participio']
        conjugations[u'6conp'] = rdict[u'6'] + u'habrían ' + conjugations[u'participio']
        # future perfect subjunctive
        conjugations[u'1fps'] = rdict[u'1'] + u'hubiere ' + conjugations[u'participio']
        conjugations[u'2fps'] = rdict[u'2'] + u'hubieres ' + conjugations[u'participio']
        conjugations[u'3fps'] = rdict[u'3'] + u'hubiere ' + conjugations[u'participio']
        conjugations[u'4fps'] = rdict[u'4'] + u'hubiéremos ' + conjugations[u'participio']
        conjugations[u'5fps'] = rdict[u'5'] + u'hubiéreis ' + conjugations[u'participio']
        conjugations[u'6fps'] = rdict[u'6'] + u'hubieren ' + conjugations[u'participio']
        # present perfect subjunctive
        conjugations[u'1pastps'] = rdict[u'1'] + u'hubiera ' + conjugations[u'participio']
        conjugations[u'2pastps'] = rdict[u'2'] + u'hubieras ' + conjugations[u'participio']
        conjugations[u'3pastps'] = rdict[u'3'] + u'hubiera ' + conjugations[u'participio']
        conjugations[u'4pastps'] = rdict[u'4'] + u'hubiéramos ' + conjugations[u'participio']
        conjugations[u'5pastps'] = rdict[u'5'] + u'hubierais ' + conjugations[u'participio']
        conjugations[u'6pastps'] = rdict[u'6'] + u'hubieran ' + conjugations[u'participio']
        # present perfect subjunctive
        conjugations[u'1presps'] = rdict[u'1'] + u'haya ' + conjugations[u'participio']
        conjugations[u'2presps'] = rdict[u'2'] + u'hayas ' + conjugations[u'participio']
        conjugations[u'3presps'] = rdict[u'3'] + u'haya ' + conjugations[u'participio']
        conjugations[u'4presps'] = rdict[u'4'] + u'hayamos ' + conjugations[u'participio']
        conjugations[u'5presps'] = rdict[u'5'] + u'hayáis ' + conjugations[u'participio']
        conjugations[u'6presps'] = rdict[u'6'] + u'hayan ' + conjugations[u'participio']

    # negative imperatives:
    if u'2pres' in conjugations:
        conjugations[u'2impn'] = u'no ' + conjugations[u'2pres']
    if u'3pres' in conjugations:
        conjugations[u'3impn'] = u'no ' + conjugations[u'3pres']
    if u'4pres' in conjugations:
        conjugations[u'4impn'] = u'no ' + conjugations[u'4pres']
    if u'5pres' in conjugations:
        conjugations[u'5impn'] = u'no ' + conjugations[u'5pres']
    if u'6pres' in conjugations:
        conjugations[u'6impn'] = u'no ' + conjugations[u'6pres']

    return conjugations

def reverse_conjugate(verb_tense):
    verb_tense = verb_tense.lower().strip()

    if is_verb(verb_tense):
        return [verb_tense]

    # first check to see if this is a known irregular verb
    if verb_tense in reverse_irregular_verbs:
        return reverse_irregular_verbs[verb_tense]

    irv, erv, arv, carv, zarv, garv = range(1, 7)

    verb_matches = {}
    all_endings = {
        1: ir_endings,
        2: er_endings,
        3: ar_endings,
        4: car_endings,
        5: zar_endings,
        6: gar_endings,
    }

    for number, endings in all_endings.items():
        for type, ending in endings.items():
            if verb_tense.endswith(ending):
                if number in verb_matches:
                    if len(ending) > len(endings[verb_matches[number]]):
                        verb_matches[number] = type
                else:
                    verb_matches[number] = type

    if not verb_matches:
        return []

    possible_verbs = []

    for number, type in verb_matches.items():
        ending = {1: u'ir', 2: u'er', 3: u'ar', 4: u'car', 5: u'zar', 6: u'gar'}[number]
        possible_verbs.append(verb_tense[:-len(ending)] + ending)

    # let's make sure the 'constructed' infinitive is a known spanish word
    return [verb for verb in possible_verbs if verb_tense in conjugate(verb).values()]

