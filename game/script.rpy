define headman = Character(_("Староста"), color="#c8ffc8")
define teacher = Character(_("Марья Ивановна"), color="#c8ffc8")

label splashscreen:
    scene black
    with Pause(1)

    show text "Дисклеймер!\nДанный проект содержит имена и сценарий, которые были полностью выдуманы авторами проекта. Любое совпадение случайно. Также содержатся изображения, которые могут негативно повлиять на ваше самочувствие. Пожалуйста, прекратите играть, если вы чувствуете дискомфорт. Спасибо." with dissolve
    with Pause(10)

    hide text with dissolve
    with Pause(1)

    show text "Приятного пробуждения" with dissolve
    with Pause(5)

    hide text with dissolve
    with Pause(1)

    return

label start:
    scene black
    play music "alarm_clock.mp3"

    "{color=#ff0000}БИП БИП БИП{/color}"
    "{i}Утро? Уже?{/i}"
    "{color=#ff0000}БИП БИП БИП{/color}"
    "{i}Надо дотянуться до телефона…{/i}"
    "{color=#ff0000}БИП БИП БИП{/color}"
    "{i}Да где же он…{/i}"
    "{color=#ff0000}БИП БИП БИП{/color}"

    scene bg dorm
    with fade
    "{i}Господи, за что мне всё это… Я снова не выспался.{/i}"

    menu:
        "Встать":
            jump get_up
        "Поспать подольше":
            jump sleep_in

label get_up:
    pass

label sleep_in:
    "{i}В пень это ваше высшее образование! Я спать хочу!{/i}"
    play music "audio/beep.mp3" noloop

    scene black
    with fade

    play music "audio/vibration.mp3"
    "{color=#ff0000}БЗЗЗ-БЗЗЗ{/color}"
    "{i}?{/i}"
    "{color=#ff0000}БЗЗЗ-БЗЗЗ{/color}"
    "{i}Я же отключил будильник… Кто-то мне звонит.{/i}"
    "{color=#ff0000}БЗЗЗ-БЗ-бип{/color}"
    play music "audio/beep.mp3" noloop

    "Алё?"
    "{color=#ff0000}СТАС, ТЫ ДУРНОЙ? ТЫ ГДЕ?{/color}"
    "{i}Это был голос старосты. Не самого нежного характером человека.{/i}"
    "Я дома"
    headman "Дома он! Ну зашибись!"
    headman "А ничего, что у нас сегодня последний день для сдачи доклада? Ты свой так и не принёс!"
    headman "А НУ МАРШ НА ПАРЫ!!"
    play music "audio/beep.mp3" noloop

    "{i}Я и слова сказать не успел. Я уже натягивал на себя штаны.{/i}"
    "{i}И как я мог забыть про дедлайн? Я же эту работу последние дня два писал.{/i}"
    "{i}Поспать подольше не удалось…{/i}"

    scene bg entrance_light
    with fade
    "{i}А вот и причина моей бессонницы, гнездо невылупившихся научных достижений, вскормленных образовательной бюрократией…?{/i}"
    "{i}...{/i}"
    "{i}О чём это я?{/i}"
    "{i}Ах да! Пора на пары.{/i}"

    scene black
    with fade
    scene bg class_entrance_light
    with fade
    scene bg class_light
    with fade
    "{i}На пару я чуть опоздал, но ничего страшного - Марья Ивановна не заметила.{/i}"
    "{i}Я тихо отсидел все 80 минут и собирался сдать доклад.{/i}"
    "{i}...{/i}"
    "{i}Как вдруг понял, что доклада-то у меня с собой и не было.{/i}"
    "{i}Я забыл его впопыхах!{/i}"
    scene bg class_seat
    with fade
    show teacher static
    with fade
    "{i}Преподавательница уже подошла ко мне, ожидая моей работы:{/i}"
    teacher ""
    "{i}...{/i}"
    ""
    show teacher silhouette
    with fade
    "{i}...{/i}"

