define headman = Character(_("Староста"), color="#c8ffc8")
define granny = Character(_("Бабушка"), color="#c8ffc8")
define teacher = Character(_("Марья Ивановна"), color="#c8ffc8")

define pause_fade = MultipleTransition(Fade(0.5, 0.0, 0.5), Pause(1.0))
define blink = Fade(0.5, 0.5, 0.5)
define travel = Fade(0.5, 1.0, 0.5)

default work = True

label splashscreen:
    scene black
    with Pause(1)

    show text "Дисклеймер!\nДанный проект содержит имена и сценарий, которые были полностью выдуманы авторами проекта. Любое совпадение случайно. Также содержатся изображения, которые могут негативно повлиять на ваше самочувствие. Пожалуйста, прекратите играть, если вы чувствуете дискомфорт. Спасибо." with dissolve
    with Pause(10)

    hide text with dissolve
    with Pause(1)

    show text "Приятного пробуждения." with dissolve
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
            $ work = False
            jump sleep_in

label get_up:
    stop music
    "{i}Надо вставать. Давай, Стас, соберись!{/i}"
    "Ну погнали."

    scene bg bus1
    with travel
    "{i}Каждое буднее утро начинается одинаково. Я просыпаюсь, не успеваю позавтракать или почистить зубы и еду на пары. Это утро ничем не отличалось....{/i}"
    "{i}В унике меня ждала очередная куча новых заданий со сроками, а потом и сессия, где я бы не спал сутками.{/i}"
    "{i}Тогда я только и мог думать о том, вот бы всё это поскорее закончилось…{/i}"
    "{i}Хотелось спать…{/i}"
    "{i}...{/i}"
    scene black
    with fade
    "???" "{color=#ff0000}ВНУЧОК{/color}"

    show granny static
    with fade
    granny "Уступи бабуле место."
    "{i}Бабка… Почему она не могла сесть куда-то ещё? В автобусе было полно свободных мест. Я только открыл рот, чтобы защитить своё право на сидение:{/i}"
    "Но там же есть ещё свободные-"
    with Pause(2)
    show granny screamer
    "???" "{color=#ff0000}УСТУПИ, Я СКАЗАЛА{/color}"

    scene bg bus2
    with fade
    "{i}Я не встал, а спрыгнул с сидения и отошёл в сторону. Бабка тут же села на моё место так, будто на нём были написаны её имя, фамилия и дата рождения.{/i}"
    "{i}А может и дата смерти, судя по её костлявым рукам.{/i}"
    "{i}Оставшиеся полчаса дороги я сидел от неё как можно дальше…{/i}"

    jump uni_entrance

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
    "???" "{color=#ff0000}СТАС, ТЫ ДУРНОЙ? ТЫ ГДЕ?{/color}"
    "{i}Это был голос старосты. Не самого нежного характером человека.{/i}"
    "Я дома"
    headman "Дома он! Ну зашибись!"
    headman "А ничего, что у нас сегодня последний день для сдачи доклада? Ты свой так и не принёс!"
    headman "А НУ МАРШ НА ПАРЫ!!"
    play music "audio/beep.mp3" noloop

    "{i}Я и слова сказать не успел. Я уже натягивал на себя штаны.{/i}"
    "{i}И как я мог забыть про дедлайн? Я же эту работу последние дня два писал.{/i}"
    "{i}Поспать подольше не удалось…{/i}"

    jump uni_entrance

label uni_entrance:
    scene bg entrance_light
    with travel
    "{i}А вот и причина моей бессонницы, гнездо невылупившихся научных достижений, вскормленных образовательной бюрократией…?{/i}"
    "{i}...{/i}"
    "{i}О чём это я?{/i}"
    "{i}Ах да! Пора на пары.{/i}"

    scene black
    with fade
    scene bg class_entrance_light
    with pause_fade
    scene bg class_light
    with pause_fade
    scene bg class_seat
    with fade
    "{i}На пару я чуть опоздал, но ничего страшного - Марья Ивановна не заметила.{/i}"
    "{i}Я тихо отсидел все 80 минут и собирался сдать доклад.{/i}"

    if work:
        jump good_work
    else:
        jump bad_work

label good_work:
    show teacher static
    with fade
    "{i}Преподавательница уже подошла ко мне, ожидая моей работы:{/i}"
    teacher "Станислав, Ваша работа?"
    "{i}Я передал ей доклад в руки и лишь на секунду встретился с ней глазами.{/i}"
    "{i}Что-то мне подсказывало, что мой ангел-хранитель спас мою жизнь, не позволив забыть этот доклад дома…{/i}"
    teacher "Спасибо..."

    teacher "Станислав, будьте добры отнести эту папку на второй этаж в учебный офис."
    scene bg table
    with fade
    "{i}Прежде чем я успел придумать отговорку или хотя бы осознать слова Марьи Ивановны,...{/i}"
    scene bg folder
    with fade
    "{i}…она уже положила передо мной красную папку с файлами и ушла{/i}"
    "Хорошо..."

    "{i}Пришлось подняться на второй этаж.{/i}"
    scene bg stairs4
    with pause_fade
    scene bg stairs3
    with pause_fade
    scene bg stairs1
    with pause_fade
    scene bg hallway1
    with pause_fade
    "{i}Я не мог вспомнить, какой из кабинетов был учебным офисом.{/i}"
    "{i}А спросить было стыдно…{/i}"
    "{i}Третий курс всё же.{/i}"

    menu:
        "Оглядеться":
            jump look_around
        "Пойти дальше":
            jump go_further

label look_around:
    pass

label go_further:
    pass

label bad_work:
    "{i}...{/i}"
    "{i}Как вдруг понял, что доклада-то у меня с собой и не было.{/i}"
    "{i}Я забыл его впопыхах!{/i}"
    show teacher static
    with fade
    "{i}Преподавательница уже подошла ко мне, ожидая моей работы:{/i}"
    teacher "Белогов, Ваша работа?"
    "{i}Вздохнув, я приготовился к раскаяниям.{/i}"
    "Я забыл её."
    show teacher silhouette
    with fade
    "{i}...{/i}"
    "{i}В глазах будто потемнело…{/i}"
    "{i}Или передо мной была уже не Марья Ивановна.{/i}"
    with Pause(2)
    show teacher eyes
    "???" "{color=#ff0000}Забыли?{/color}"
    show teacher screamer
    with Pause(3)
    scene black
    with fade

    return
