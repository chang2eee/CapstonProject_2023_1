import hanspell.spell_checker

sent = "맞춤법이 틀린 문장이 돼었습니다."
spelled_sent = hanspell.spell_checker.check(sent)

hanspell_sent = spelled_sent.checked
print(hanspell_sent)