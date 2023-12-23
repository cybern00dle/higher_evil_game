init python:
    renpy.music.register_channel("long_sfx", "sfx", True)
    renpy.music.register_channel("screamer", "sfx", True)

define headman = Character(_("Староста"), color="#ff6971")
define granny = Character(_("Бабушка"), color="#ff6971")
define teacher = Character(_("Марья Ивановна"), color="#ff6971")
define cultist = Character(_("Культист"), color="#ff6971")
define guard = Character(_("Охранник"), color="#ff6971")

define circling = MultipleTransition([
    False, fade, "bg ground1_dark.png",
    Pause(1.0), "bg ground1_dark.png",
    fade, "bg ground3_dark.png",
    Pause(1.0), "bg ground1_dark.png",
    fade, "bg hallway6_dark.png",
    Pause(1.0), "bg ground1_dark.png",
    fade, True])
define death_screen = MultipleTransition([False, Pause(3), False, fade, True])
define pause_fade = MultipleTransition([False, fade, True, Pause(1.0), True])
define blink = Fade(0.5, 0.5, 0.5)
define travel = Fade(0.5, 1.0, 0.5)

default flashlight = False
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

    show text "Мяу." with dissolve
    with Pause(5)

    hide text with dissolve
    with Pause(1)

    return

label start:
    scene black
    play long_sfx "alarm_clock.mp3" volume 0.5

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
    stop long_sfx
    play sound "audio/beep.mp3"
    "{i}Надо вставать. Давай, Стас, соберись!{/i}"
    "Ну погнали."

    scene bg bus1
    with travel
    play long_sfx "audio/bus.mp3" volume 0.5
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
    play screamer "audio/static.mp3"
    show granny screamer
    "???" "{color=#ff0000}УСТУПИ, Я СКАЗАЛА{/color}"
    stop screamer

    scene bg bus2
    with fade
    "{i}Я не встал, а спрыгнул с сидения и отошёл в сторону. Бабка тут же села на моё место так, будто на нём были написаны её имя, фамилия и дата рождения.{/i}"
    "{i}А может и дата смерти, судя по её костлявым рукам.{/i}"
    "{i}Оставшиеся полчаса дороги я сидел от неё как можно дальше…{/i}"

    jump uni_entrance

label sleep_in:
    "{i}В пень это ваше высшее образование! Я спать хочу!{/i}"
    stop long_sfx
    play sound "audio/beep.mp3"

    scene black
    with fade
    play long_sfx "audio/vibration.mp3"
    "{color=#ff0000}БЗЗЗ-БЗЗЗ{/color}"
    "{i}?{/i}"
    "{color=#ff0000}БЗЗЗ-БЗЗЗ{/color}"
    "{i}Я же отключил будильник… Кто-то мне звонит.{/i}"
    "{color=#ff0000}БЗЗЗ-БЗ-бип{/color}"
    stop long_sfx
    play sound "audio/beep.mp3"

    "Алё?"
    "???" "{color=#ff0000}СТАС, ТЫ ДУРНОЙ? ТЫ ГДЕ?{/color}"
    "{i}Это был голос старосты. Не самого нежного характером человека.{/i}"
    "Я дома"
    headman "Дома он! Ну зашибись!"
    headman "А ничего, что у нас сегодня последний день для сдачи доклада? Ты свой так и не принёс!"
    headman "А НУ МАРШ НА ПАРЫ!!"
    play sound "audio/beep.mp3"

    "{i}Я и слова сказать не успел. Я уже натягивал на себя штаны.{/i}"
    "{i}И как я мог забыть про дедлайн? Я же эту работу последние дня два писал.{/i}"
    "{i}Поспать подольше не удалось…{/i}"

    jump uni_entrance

label uni_entrance:
    play music "audio/theme.mp3"
    scene bg entrance
    with travel
    "{i}А вот и причина моей бессонницы, гнездо невылупившихся научных достижений, вскормленных образовательной бюрократией…?{/i}"
    "{i}...{/i}"
    "{i}О чём это я?{/i}"
    "{i}Ах да! Пора на пары.{/i}"

    play long_sfx "audio/walk.mp3"
    scene black
    with fade
    scene bg class_entrance
    with pause_fade
    scene bg class_room
    with pause_fade
    scene bg class_seat
    with fade
    stop long_sfx
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
    play sound "audio/hand.mp3"
    scene bg table
    with fade
    "{i}Прежде чем я успел придумать отговорку или хотя бы осознать слова Марьи Ивановны...{/i}"
    play sound "audio/drop.mp3"
    scene bg folder
    with fade
    "{i}…она уже положила передо мной красную папку с файлами и ушла{/i}"
    "Хорошо..."

    "{i}Пришлось подняться на второй этаж.{/i}"
    play long_sfx "audio/walk.mp3"
    scene bg stairs4
    with pause_fade
    scene bg stairs3
    with pause_fade
    scene bg stairs1
    with pause_fade
    scene bg hallway1
    with pause_fade
    stop long_sfx
    "{i}Я не мог вспомнить, какой из кабинетов был учебным офисом.{/i}"
    "{i}А спросить было стыдно…{/i}"
    "{i}Третий курс всё же.{/i}"

    menu:
        "Оглядеться":
            jump look_around
        "Пойти дальше":
            jump go_further

label look_around:
    "{i}Я огляделся.{/i}"
    scene bg hallway1
    with fade
    stop music
    "{i}...{/i}"
    show monster static
    with fade
    play music "audio/dark_hallways.mp3"
    "{i}!!!{/i}"
    "{i}Я замер.{/i}"
    "{i}Нет-{/i}"
    "{i}Застыл...{/i}"
    show monster dark
    "{i}То ли у меня потемнело в глазах, то ли в коридоре погас свет.{/i}"
    "{i}Мразь смотрела на меня молчаливо и бездвижно… У меня подкосились ноги.{/i}"

    menu:
        "Бежать":
            jump run
        "Поздороваться":
            jump greet

label run:
    play screamer "audio/static.mp3"
    show monster screamer
    "{i}НУ НАФИГ{/i}"
    play music "audio/chase.mp3" volume 0.5
    stop screamer
    play long_sfx "audio/run.mp3"
    scene bg stairs1
    with pause_fade
    scene bg stairs3
    with pause_fade
    scene bg stairs4
    with pause_fade
    scene bg ground2
    with pause_fade
    stop long_sfx

    play music "audio/dark_hallways.mp3"
    "{i}...{/i}"
    "{i}Я остановился.{/i}"
    "{i}...{/i}"
    "{i}Оно не последовало за мной.{/i}"
    "{i}Я только хотел выдохнуть и возможно бросить неприличное слово...{/i}"
    scene bg ground2_dark
    with blink
    "{i}…как вдруг погас свет.{/i}"
    "Ну нет… Наверх я точно один не пойду."
    "{i}Я боялся, что та тварь всё ещё там.{/i}"
    "Надо найти хоть кого-то здесь."

    play long_sfx "audio/walk.mp3"
    show bg ground1_dark
    with circling
    stop long_sfx
    "..."
    "Это что щас было?"
    "Я же уже здесь был…"
    "{i}Я потерялся и решил попробовать пройтись по этажу снова.{/i}"
    play long_sfx "audio/walk.mp3"
    show bg ground1_dark
    with circling
    stop long_sfx
    "Да какого чёрта?!"
    "{i}Я ходил кругами и был уже на пределе.{/i}"
    "{i}Я был напуган до усрачки, хотел спать и просто вернуться домой!{/i}"
    "{i}Хотелось, чтобы вся жуть, что я увидел, была простым сном.{/i}"
    "{i}От одной мысли о сне мои глаза начали слипаться…{/i}"
    "{i}...{/i}"

    show cult corner
    with blink
    "{i}Человек.{/i}"
    "{i}Человек!{/i}"
    "{i}Я уже хотел крикнуть от радости и позвать незнакомца на помощь-{/i}"
    show cult static
    with fade
    "{i}-но он подошёл ко мне сам.{/i}"
    cultist "Что ты здесь шастаешь?"
    "{i}Говорил он со мной явно недружелюбно. Я даже проснулся от его резкого тона и впервые в жизни начал заикаться.{/i}"
    "Т-т-т-т-там б-была хрень к-к-какая-то. Я по-побежал, а потом п-пытался найти хоть кого-то!"
    "Здесь лабиринт! Я-я поворачиваю - то же самое, поворачиваю - снова-"
    "{i}Выражение на лице незнакомца совсем не поменялось от моего рассказа.{/i}"
    "{i}Мне даже показалось, что он с таким сталкивается не в первый раз.{/i}"
    cultist "Сынок, ты просто устал. Мало ли, что может с такими кругами под глазами почудиться."
    "{i}А вот тон его изменился. Стал нежнее.{/i}"
    "{i}Мне это не понравилось… Я замешкался под его взглядом.{/i}"
    "{i}Только сейчас я заметил, во что он был одет: то ли накидка, то ли фата.{/i}"
    "{i}Своим нарядом он напоминал птицу.{/i}"
    "Помогите мне выбраться отсюда."
    "{i}Я будто молил его.{/i}"
    "{i}Унижаться было неприятно, но я был в отчаянии.{/i}"
    show cult close_up
    with fade
    cultist "Конечно, мы тебе поможем."
    "{i}Я подумал, что не расслышал его.{/i}"
    "Мы?"
    stop music
    with Pause(2)
    play screamer "audio/static.mp3"
    show cult screamer
    cultist "{color=#ff0000}МЫ, ПРАВЫЕ ПОСЛЕДОВАТЕЛИ ВОРОНА, ВСЕГДА ПОМОГАЕМ ЗАБЛУДШИМ ДУШАМ{/color}"
    scene black
    with death_screen
    stop screamer

    jump you_died

label greet:
    "{i}Я сглотнул, прежде чем открыл рот.{/i}"
    "З-здравствуйте."
    "{i}Я заикался впервые в жизни.{/i}"
    show monster static
    with fade
    "{i}!{/i}"
    scene black
    with fade
    "{i}От яркого света у меня заболели глаза и я прикрыл их лишь на секунду.{/i}"
    play music "audio/theme.mp3"
    show motster human
    with fade
    "{i}А когда я их открыл, передо мной уже стоял менеджер нашего потока…{/i}"
    "Здравствуйте."
    "{i}Он был будто неживой, а точнее просто уставший.{/i}"
    "{i}Я, конечно, его хорошо понимал и хотел даже пожалеть, но мои мысли были заняты видом той твари, что я только что видел.{/i}"
    "{i}Я даже не заметил, как менеджер взял папку из моих рук…{/i}"
    scene bg hallway1
    with fade
    "{i}…и ушёл.{/i}"
    "{i}Я стоял там в недоумении и холодном поту ещё пару минут, пока не решил списать этот бред на недосып и просто пойти на следующую пару.{/i}"

    jump study

label go_further:
    "{i}Я решил пойти в одном направлении, пока не вспомню номер кабинета.{/i}"
    play long_sfx "audio/walk.mp3"
    scene bg hallway2
    with pause_fade
    scene bg hallway4
    with pause_fade
    scene bg door_closed
    with pause_fade
    stop long_sfx
    play music "audio/theme.mp3"
    "Вроде здесь."
    play long_sfx "audio/chewing.mp3"
    "{i}Всё бы ничего, но я слышал странные звуки, идущие из кабинета.{/i}"
    "{i}Чавканье?{/i}"
    "{i}Узнать наверняка можно было лишь одним способом…{/i}"
    stop long_sfx

    menu:
        "Зайти":
            jump enter
        "Постучаться":
            jump knock

label enter:
    "{i}Любопытство победило, и я бесцеремонно зашёл внутрь.{/i}"
    show creature back
    with fade
    "{i}Что ж… Это был не учебный офис, а самая обычная аудитория.{/i}"
    "{i}Было темно, поэтому сначала я ничего не разглядел. Но потом я увидел чей-то огромный силуэт в конце аудитории.{/i}"
    "{i}Кроме того, в аудитории стоял ужасный запах.{/i}"
    "{i}Мне стало не по себе, начала кружится голова…{/i}"
    show creature static
    with blink
    "{i}!!!{/i}"
    "{i}Вонь стала ещё пронзительнее.{/i}"
    "{i}От страха и отвращения у меня подкосило ноги.{/i}"
    "{i}Бежать я не мог - меня будто парализовало.{/i}"
    "П-"
    "Помогите!"
    stop music
    with Pause(2)
    play screamer "audio/static.mp3"
    show creature screamer
    scene black
    with death_screen
    stop screamer

    jump you_died

label knock:
    "Всё-таки заходить без стука нельзя… Меня же не в пещере растили."
    play sound "audio/knock.mp3"
    "{i}Я постучался и за дверью тут же послышался неловкий шорох. Будто кто-то бегал по кабинету, пытаясь найти, откуда прозвучал стук.{/i}"
    play sound "audio/knock.mp3"
    "{i}Я постучал ещё разок и дверь тут же приоткрылась.{/i}"
    play sound "audio/creaking.mp3"
    show face static
    with fade
    "{i}!{/i}"
    "{i}Я чуть вздрогнул от неожиданности.{/i}"
    "{i}Незнакомец смотрел на меня бдительно около минуты, ничего не говоря...{/i}"
    play sound "audio/hand.mp3"
    scene bg door_open
    with fade
    "{i}…а потом скрылся.{/i}"
    play sound "audio/hand.mp3"
    show face hand
    with fade
    "{i}Вместо него показалась рука в довольно странном положении.{/i}"
    "{i}Я предположил, что он ждал, когда я отдам ему папку.{/i}"
    play sound "audio/drop.mp3"
    show face folder
    "{i}Ну я её и положил.{/i}"
    play sound "audio/hand.mp3"
    scene bg door_open
    with fade
    "{i}Рука тут же исчезла за дверью вместе с папкой.{/i}"
    "{i}Я был готов уходить, но услышал уже знакомый шорох.{/i}"
    play sound "audio/hand.mp3"
    show face flashlight
    with fade
    "{i}Фонарик?{/i}"
    "{i}Я недоумевал, зачем он мне и почему мне его вообще дают.{/i}"
    "{i}Но отказываться, мне казалось, было бы грубо.{/i}"

    $ flashlight = True
    play sound "audio/hand.mp3"
    show face hand
    with Pause(0.5)
    play sound "audio/creaking.mp3"
    scene bg door_closed
    with fade
    "{i}Это было…{/i}"
    "{i}…странно.{/i}"
    "{i}Но я решил списать неловкое чувство на сонливость и пойти на следующие пары.{/i}"

    jump study

label study:
    play music "audio/theme.mp3"
    scene black
    with fade
    "{i}Весь день я сидел на парах, пытался заработать накоп на семинарах и хоть что-то законспектировать на лекциях.{/i}"
    "{i}И весь день мне хотелось спать…{/i}"
    "{i}В один момент я был настолько измотан, что, похоже, вырубился прямо на паре.{/i}"
    play music "audio/dark_hallways.mp3"
    scene bg class007
    with fade
    "{i}А когда проснулся, то в аудитории уже никого не было…{/i}"
    "Меня просто оставили здесь."
    "{i}Не было сил даже на то, чтобы возмущаться. Хотелось просто, наконец-то, уйти домой.{/i}"
    scene bg hallway2_dark
    with fade
    "{i}Было темно…{/i}"
    "Неужели все уже ушли?"
    show stair_creature dark
    with fade
    "{i}?!{/i}"
    "{i}Человек?{/i}"
    "{i}На человека оно не было похожим.{/i}"
    "{i}Скорее на его останки.{/i}"
    "{i}Я решил пройти мимо этого нечто так, чтобы оно не заметило меня.{/i}"
    scene bg stairs4_dark
    with fade
    "{i}Медленно и тихо крадясь, я добрался до первого этажа.{/i}"
    "{i}Я выдохнул с облегчением…{/i}"
    show stair_creature follow
    with fade
    "{i}…пока не увидел, что оно начало меня преследовать.{/i}"
    play music "audio/chase.mp3" volume 0.5
    play long_sfx "audio/run.mp3"
    scene bg exit1_dark
    with fade
    "{i}Я побежал к выходу.{/i}"
    scene bg exit2_dark
    with fade
    "{i}!{/i}"
    "{i}Заперто!{/i}"
    "{i}Были слышны его шаги. Оно приближалось.{/i}"
    scene bg defense_door
    with fade
    "{i}Я подбежал к двери, которая отделяла меня и чудище и схватился за ручку, уперевшись ногой в дверную раму.{/i}"
    play long_sfx "audio/bang.mp3" volume 2
    show doorman knock
    "{i}Оно билось в дверное стекло, не жалея себя или меня.{/i}"
    "{color=#ff0000}БУМ БУМ БУМ{/color}"
    "{i}Моих сил явно не хватало.{/i}"

    if flashlight:
        jump good_ending
    else:
        jump creature_trap

label good_ending:
    "{i}Надежды на то, что я смогу продержаться ещё хоть секунду, не было.{/i}"
    stop long_sfx
    "{i}Отпустив ручку двери, я схватил первое попавшееся, чем мог защитить себя.{/i}"
    "{i}Фонарик.{/i}"
    play sound "audio/flashlight.mp3" volume 2
    "{i}Я включил его совершенно случайно.{/i}"
    show doorman light
    with fade
    scene bg defense_light
    with fade
    play sound "audio/run_away.mp3" volume 2
    play sound "audio/run.mp3"
    "{i}Тварь, что так яростно долбилась в дверь, сбежала с воплями.{/i}"
    "{i}...{/i}"
    "{i}Я сидел с включённым фонариком, ощущая стекающий с себя холодный пот ещё минуту, пока не пришёл охранник.{/i}"

    play music "audio/theme.mp3"
    show guard static
    guard "Парень, ты чё тут делаешь?"
    "{i}Я уже не был уверен, что со мной разговаривает человек.{/i}"
    guard "А ну марш домой! Нечего в вузе ночью делать."
    "{i}Он спокойной открыл ключами ранее запертую дверь и распахнул её перед моим носом.{/i}"
    "{i}Я сбежал оттуда так быстро, как только мог…{/i}"

    scene bg dorm_dark
    with travel
    "Я дома..."
    "{i}Мечтая забыть, что я сегодня пережил, я бросил свою измученную тушу на кровать.{/i}"
    scene black
    with fade
    "{i}Это всё из-за бессонницы...{/i}"
    stop music

    jump you_won

label creature_trap:
    "{color=#ff0000}БУМ БУМ БУМ{/color}"
    "{i}Я больше не мог держать дверь-{/i}"
    stop long_sfx
    with Pause(2)
    play screamer "audio/scream.mp3"
    show doorman screamer
    scene black
    with death_screen
    stop screamer

    jump you_died

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
    stop music
    with Pause(2)
    show teacher eyes
    "???" "{color=#ff0000}Забыли?{/color}"
    play screamer "audio/static.mp3"
    show teacher screamer
    scene black
    with death_screen
    stop screamer

    jump you_died

label you_won:
    scene black
    with Pause(1)

    show text "Приятных сновидений" with dissolve
    with Pause(2)

    show text "Игра пройдена" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label you_died:
    scene black
    with Pause(1)

    show text "{color=#ff0000}Игра окончена{/color}" with dissolve
    with Pause(5)

    hide text with dissolve
    with Pause(1)

    return
