# 2. В большой текстовой строке подсчитать количество встречаемых слов
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# (Может помочь метод translate из модуля string)

import re
from collections import Counter

def top_10(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = """Сказка о рыбаке и рыбке
Жил старик со своею старухой
У самого синего моря;
Они жили в ветхой землянке
Ровно тридцать лет и три года.
Старик ловил неводом рыбу,
Старуха пряла свою пряжу.
Раз он в море закинул невод, —
Пришел невод с одною тиной.
Он в другой раз закинул невод, —
Пришел невод с травой морскою.
В третий раз закинул он невод, —
Пришел невод с одною рыбкой,
С непростою рыбкой, — золотою.
Как взмолится золотая рыбка!
Голосом молвит человечьим:

«Отпусти ты, старче, меня в море,
Дорогой за себя дам откуп:
Откуплюсь чем только пожелаешь».
Удивился старик, испугался:
Он рыбачил тридцать лет и три года
И не слыхивал, чтоб рыба говорила.
Отпустил он рыбку золотую
И сказал ей ласковое слово:
«Бог с тобою, золотая рыбка!
Твоего мне откупа не надо;
Ступай себе в синее море,
Гуляй там себе на просторе»."""
print(top_10(text))