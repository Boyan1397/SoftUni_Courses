#пишем petterna по който ще търсим даден тескст(//.data.//.data//)
# с pattern(шаблон) се търси съвпадение на даден текст
#SPECIAL SEQUENCES
# \d ONLY digits
# \D NOT digits
#\b  е начало или край|||започва с или завършва с както в преимера отдолу
# не искам да има букви преди или след него
# \b\d навсякъде където започва с число
# \d\b навсякъде където звършва с число
#\S търси всичко без  space and tab
# \S noot whitespace ili tab
# \s whitespace или tabs
#\w  търси letters, digits, И _ включително!!!!
# \w letters digits И _ включително
# \W само знаци без _
#METACHARACTERS
# . = any
# * zero or more
# + = one or more
# | = gives both
# () = group
# ^ = startswith конкретно
# % = endswith конкретно
#sets
# [arn] = a or r or not
# ^[arn] =  всичко без  ar
# [a-n] = alphabetically - ascii
# [A-Z][a-z] = start with capital and continue with lower

#pythex functions
# ignorancecase = lower or upper doesnt matter
# multiline =   използваме когато е ред по ред
