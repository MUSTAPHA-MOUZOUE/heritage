from tkinter import *
from tkinter import Tk as tk 
# from QuotePages import Page_setting 

Topics = ["ميسر بتفسير آيات ","      الإرث   قسمة  "] 
Choices = ["male", "female"]


page_num = 0
Quote = ["۞﴾233﴿سورة البقرة\nوَالْوَالِدَاتُ يُرْضِعْنَ أَوْلَادَهُنَّ حَوْلَيْنِ كَامِلَيْنِ لِمَنْ أَرَادَ أَن يُتِمَّ \nالرَّضَاعَةَ  وَعَلَى الْمَوْلُودِ لَهُ رِزْقُهُنَّ وَكِسْوَتُهُنَّ بِالْمَعْرُوفِ \n لَا تُكَلَّفُ نَفْسٌ إِلَّا وُسْعَهَا  لَا تُضَارَّ وَالِدَةٌ بِوَلَدِهَا وَلَا مَوْلُودٌ\n لَّهُ بِوَلَدِهِ  وَعَلَى الْوَارِثِ مِثْلُ ذَٰلِكَ فَإِنْ أَرَادَا فِصَالًا عَن تَرَاضٍ \nمِّنْهُمَا وَتَشَاوُرٍ فَلَا جُنَاحَ عَلَيْهِمَا وَإِنْ أَرَدتُّمْ \nأَن تَسْتَرْضِعُوا أَوْلَادَكُمْ فَلَا جُنَاحَ عَلَيْكُمْ إِذَا سَلَّمْتُم مَّا آتَيْتُم\n بِالْمَعْرُوفِ وَاتَّقُوا اللَّهَ وَاعْلَمُوا أَنَّ اللَّهَ بِمَا تَعْمَلُونَ بَصِيرٌ",
"۞﴾7﴿سورة النساء\n\nلِّلرِّجَالِ نَصِيبٌ مِّمَّا تَرَكَ الْوَالِدَانِ وَالْأَقْرَبُونَ  \n وَلِلنِّسَاءِ نَصِيبٌ مِّمَّا تَرَكَ الْوَالِدَانِ وَالْأَقْرَبُونَ \n مِمَّا قَلَّ مِنْهُ أَوْ كَثُرَ نَصِيبًا مَّفْرُوضًا ",
"۞﴾8﴿سورة النساء\n\nوَإِذَا حَضَرَ الْقِسْمَةَ أُولُو الْقُرْبَىٰ وَالْيَتَامَىٰ وَالْمَسَاكِينُ \n فَارْزُقُوهُم مِّنْهُ وَقُولُوا لَهُمْ قَوْلًا مَّعْرُوفًا",
"۞﴾9﴿سورة النساء\n\nوَلْيَخْشَ الَّذِينَ لَوْ تَرَكُوا مِنْ خَلْفِهِمْ ذُرِّيَّةً ضِعَافًا \nخَافُوا عَلَيْهِمْ فَلْيَتَّقُوا اللَّهَ وَلْيَقُولُوا قَوْلًا سَدِيدًا",
"۞﴾11﴿سورة النساء \nيُوصِيكُمُ اللَّهُ فِي أَوْلَادِكُمْ لِلذَّكَرِ مِثْلُ حَظِّ الْأُنثَيَيْنِ فَإِن كُنَّ \n نِسَاءً اثْنَتَيْنِ فَلَهُنَّ ثُلُثَا مَا تَرَكَ وَإِن كَانَتْ وَاحِدَةً فَلَهَا \nالنِّصْفُ وَلِأَبَوَيْهِ لِكُلِّ وَاحِدٍ مِّنْهُمَا السُّدُسُ مِمَّا تَرَكَ \nإِن كَانَ لَهُ وَلَدٌ فَإِن لَّمْ يَكُن لَّهُ وَلَدٌ وَوَرِثَهُ أَبَوَاهُ \nفَلِأُمِّهِ الثُّلُثُ فَإِن كَانَ لَهُ إِخْوَةٌ فَلِأُمِّهِ السُّدُسُ مِن بَعْدِ وَصِيَّةٍ\n يُوصِي بِهَا أَوْ دَيْنٍ آبَاؤُكُمْ وَأَبْنَاؤُكُمْ لَا تَدْرُونَ أَيُّهُمْ أَقْرَبُ لَكُمْ\n نَفْعًا فَرِيضَةً مِّنَ اللَّهِ إِنَّ اللَّهَ كَانَ عَلِيمًا حَكِيمًا",
"سورة النساء﴿12 ﴾  وَلَكُمْ نِصْفُ مَا تَرَكَ أَزْوَاجُكُمْ إِن لَّمْ \nيَكُن لَّهُنَّ وَلَدٌ فَإِن كَانَ لَهُنَّ وَلَدٌ فَلَكُمُ الرُّبُعُ مِمَّا تَرَكْنَ مِن\n بَعْدِ وَصِيَّةٍ يُوصِينَ بِهَا أَوْ دَيْنٍ وَلَهُنَّ الرُّبُعُ مِمَّا تَرَكْتُمْ\n إِن لَّمْ يَكُن لَّكُمْ وَلَدٌ فَإِن كَانَ لَكُمْ وَلَدٌ فَلَهُنَّ الثُّمُنُ مِمَّا تَرَكْتُم\n مِّن بَعْدِ وَصِيَّةٍ تُوصُونَ بِهَا أَوْ دَيْنٍ وَإِن كَانَ رَجُلٌ يُورَثُ\n كَلَالَةً أَوِ امْرَأَةٌ وَلَهُ أَخٌ أَوْ أُخْتٌ فَلِكُلِّ وَاحِدٍ مِّنْهُمَا السُّدُسُ\n فَإِن كَانُوا أَكْثَرَ مِن ذَٰلِكَ فَهُمْ شُرَكَاءُ فِي الثُّلُثِ مِن بَعْدِ وَصِيَّةٍ \nيُوصَىٰ بِهَا أَوْ دَيْنٍ غَيْرَ مُضَارٍّ وَصِيَّةً مِّنَ اللَّهِ وَاللَّهُ عَلِيمٌ حَلِيمٌ",
"۞﴾19﴿سورة النساء\n\nيَا أَيُّهَا الَّذِينَ آمَنُوا لَا يَحِلُّ لَكُمْ أَن تَرِثُوا النِّسَاءَ كَرْهًا\n وَلَا تَعْضُلُوهُنَّ لِتَذْهَبُوا بِبَعْضِ مَا آتَيْتُمُوهُنَّ \nإِلَّا أَن يَأْتِينَ بِفَاحِشَةٍ مُّبَيِّنَةٍ  وَعَاشِرُوهُنَّ بِالْمَعْرُوفِ  \nفَإِن كَرِهْتُمُوهُنَّ فَعَسَىٰ أَن تَكْرَهُوا شَيْئًا\n وَيَجْعَلَ اللَّهُ فِيهِ خَيْرًا كَثِيرًا",
"۞﴾33﴿سورة النساء\n\nوَلِكُلٍّ جَعَلْنَا مَوَالِيَ مِمَّا تَرَكَ الْوَالِدَانِ وَالْأَقْرَبُونَ\n وَالَّذِينَ عَقَدَتْ أَيْمَانُكُمْ فَآتُوهُمْ نَصِيبَهُمْ  \nإِنَّ اللَّهَ كَانَ عَلَىٰ كُلِّ شَيْءٍ شَهِيدًا",
"۞﴾127﴿سورة النساء\n\nوَيَسْتَفْتُونَكَ فِي النِّسَاءِ\n قُلِ اللَّهُ يُفْتِيكُمْ فِيهِنَّ وَمَا يُتْلَىٰ عَلَيْكُمْ فِي الْكِتَابِ \nفِي يَتَامَى النِّسَاءِ اللَّاتِي لَا تُؤْتُونَهُنَّ \nمَا كُتِبَ لَهُنَّ وَتَرْغَبُونَ أَن تَنكِحُوهُنَّ \nوَالْمُسْتَضْعَفِينَ مِنَ الْوِلْدَانِ وَأَن تَقُومُوا لِلْيَتَامَىٰ بِالْقِسْطِ\n وَمَا تَفْعَلُوا مِنْ خَيْرٍ فَإِنَّ اللَّهَ كَانَ بِهِ عَلِيمًا",
"۞﴾176﴿سورة النساء\n\nيَسْتَفْتُونَكَ قُلِ اللَّهُ يُفْتِيكُمْ فِي الْكَلَالَةِ\n إِنِ امْرُؤٌ هَلَكَ لَيْسَ لَهُ وَلَدٌ وَلَهُ أُخْتٌ فَلَهَا نِصْفُ مَا تَرَكَ\n وَهُوَ يَرِثُهَا إِن لَّمْ يَكُن لَّهَا وَلَدٌ\n فَإِن كَانَتَا اثْنَتَيْنِ فَلَهُمَا الثُّلُثَانِ مِمَّا تَرَكَ وَإِن كَانُوا \nإِخْوَةً رِّجَالًا وَنِسَاءً فَلِلذَّكَرِ مِثْلُ حَظِّ الْأُنثَيَيْنِ\n يُبَيِّنُ اللَّهُ لَكُمْ أَن تَضِلُّوا وَاللَّهُ بِكُلِّ شَيْءٍ عَلِيمٌ"]
definition = ["على الوالدات إرضاع أولادهن مدة سنتين\n كاملتين لمن أراد إتمام الرضاعة\n ويجب على الآباء أن يكفُلوا للمرضعات \nالمطلقات طعامهن وكسوتهن على الوجه \nالمستحسن شرعًا وعرفًا لأن الله لا يكلف نفسًا\n إلا قدر طاقتها ولا يحل للوالدين أن يجعلوا \nالمولود وسيلة للمضارة بينهما \nويجب على الوارث عند موت الوالد\n مثل ما يجب على الوالد قبل موته\n من النفقة والكسوة. فإن أراد \nالوالدان فطام المولود قبل انتهاء \nالسنتين فلا حرج عليهما إذا تراضيا \nوتشاورا في ذلك؛ ليصلا إلى ما فيه\n مصلحة المولود. وإن اتفق الوالدان \nعلى إرضاع المولود من مرضعة أخرى\n غير والدته فلا حرج عليهما إذا\n سلَّم الوالد للأم حقَّها وسلَّم للمرضعة\n أجرها بما يتعارفه الناس. وخافوا\n الله في جميع أحوالكم واعلموا\n أن الله بما تعملون بصير\n وسيجازيكم على ذلك",
"للذكور صغارًا أو كبارًا نصيب\n شرعه الله فيما تركه الوالدان\n والأقربون من المال قليلا\n كان أو كثيرًا في أنصبة\n محددة واضحة فرضها الله \nعز وجل لهؤلاء وللنساء كذلك",
"وإذا حضر قسمةَ الميراث أقاربُ\n الميت ممن لا حقَّ لهم في التركة \nأو حضرها من مات آباؤهم وهم صغار\n أو مَن لا مال لهم فأعطوهم شيئًا\n من المال على وجه الاستحباب قبل\n تقسيم التركة على أصحابها\n وقولوا لهم قولا حسنًا غير فاحش ولا قبيح",
"ولْيَخَفِ الذين لو ماتوا وتركوا\n من خلفهم أبناء صغارًا ضعافًا خافوا \nعليهم الظلم والضياع فليراقبوا\n الله فيمن تحت أيديهم من اليتامى \nوغيرهم وذلك بحفظ أموالهم وحسن\n تربيتهم ودَفْع الأذى عنهم وليقولوا\n لهم قولا موافقا للعدل والمعروف.",
"يوصيكم الله ويأمركم في شأن أولادكم\n إذا مات أحد منكم وترك أولادًا ذكورًا وإناثًا\n فميراثه كله لهم للذكر مثل نصيب الأنثيين\n إذا لم يكن هناك وارث غيرهم فإن ترك بنات \nفقط فللبنتين فأكثر ثلثا ما ترك وإن كانت ابنة\n واحدة فلها النصف ولوالِدَي الميت لكل\n واحد منهما السدس إن كان له ولد ذكرًا\n كان أو أنثى واحدًا أو أكثر فإن لم يكن\n له ولد وورثه والداه فلأمه الثلث ولأبيه\n الباقي فإن كان للميت إخوة اثنان فأكثر\n ذكورًا كانوا أو إناثًا فلأمه السدس وللأب \nالباقي ولا شيء للإخوة وهذا التقسيم للتركة\n إنما يكون بعد إخراج وصية الميت في حدود \nالثلث أو إخراج ما عليه من دَيْن آباؤكم \nوأبْناؤكم الذين فُرِض لهم الإرث لا تعرفون أيهم\n أقرب لكم نفعًا في دنياكم وأخراكم فلا تفضلوا \nواحدًا منهم على الآخر هذا الذي أوصيتكم به\n مفروض عليكم من الله إن الله كان\n عليمًا بخلقه حكيمًا فيما شرعه لهم",
"ولكم أيها الرجال نصف ما ترك أزواجكم\n بعد وفاتهن إن لم يكن لهن ولد ذكرًا كان\n أو أنثى فإن كان لهن ولد فلكم الربع مما تركن\n ترثونه من بعد إنفاذ وصيتهن الجائزة أو\n ما يكون عليهن من دَيْن لمستحقيه. ولأزواجكم\n أيها الرجال الربع مما تركتم إن لم يكن لكم\n ابن أو ابنة منهن أو من غيرهن فإن كان لكم\n ابن أو ابنة فلهن الثمن مما تركتم يقسم الربع \nأو الثمن بينهن فإن كانت زوجة واحدة كان\n هذا ميراثًا لها من بعد إنفاذ ما كنتم أوصيتم به\n من الوصايا الجائزة أو قضاء ما يكون عليكم\n من دَيْن. وإن مات رجل أو امراة وليس له\n أو لها ولد ولا والد وله أو لها أخ أو\n أخت من أم فلكل واحد منهما السدس. فإن كان \nالإخوة أو الأخوات لأم أكثر من ذلك فهم شركاء\n في الثلث يقسم بينهم بالسوية لا فرق بين \nالذكر والأنثى وهذا الذي فرضه الله للإخوة \nوالأخوات لأم يأخذونه ميراثًا لهم من بعد قضاء\n ديون الميت وإنفاذ وصيته إن كان قد\n أوصى بشيء لا ضرر فيه على الورثة. بهذا \n أوصاكم ربكم وصية نافعة لكم ",
"يا أيها الذين آمنوا لا يجوز لكم\n أن تجعلوا نساء آبائكم من جملة \nتَرِكتهم تتصرفون فيهن بالزواج منهن\n أو المنع لهن أو تزويجهن للآخرين\n وهن كارهات لذلك كله ولا يجوز لكم\n أن تضارُّوا أزواجكم وأنتم كارهون لهن\n ليتنازلن عن بعض ما آتيتموهن من مهر ونحوه\n إلا أن يرتكبن أمرا فاحشا كالزنى فلكم\n حينئذ إمساكهن حتى تأخذوا ما أعطيتموهن\n ولتكن مصاحبتكم لنسائكم مبنية على التكريم و\nالمحبة وأداء ما لهن من حقوق فإن كرهتموهن\n لسبب من الأسباب الدنيوية فاصبروا فعسى \nأن تكرهوا أمرًا من الأمور ويكون فيه خير كثير",
"ولكل واحد منكم جعلنا ورثة يرثون\n مما ترك الوالدان والأقربون والذين\n تحالفتم معهم بالأيمان المؤكدة على النصرة\n وإعطائهم شيئًا من الميراث فأعطوهم \nما قُدِّر لهم والميراث بالتحالف كان\n في أول الإسلام ثم رُفع حكمه بنزول آيات \nالمواريث إن الله كان مُطَّلِعًا على \nكل شيء من أعمالكم وسيجازيكم على ذلك",
"يطلب الناس منك أيها النبي \nأن تبين لهم ما أشكل عليهم فَهْمُه من قضايا \nالنساء وأحكامهن قل الله تعالى يبيِّن\n لكم أمورهن وما يتلى عليكم في الكتاب\n في يتامى النساء اللاتي لا تعطونهن ما فرض\n الله تعالى لهن من المهر والميراث \nوغير ذلك من الحقوق وتحبون نكاحهن أو \nترغبون عن نكاحهن ويبيِّن الله لكم أمر \nالضعفاء من الصغار ووجوب القيام لليتامى\n بالعدل وترك الجور عليهم في حقوقهم\n وما تفعلوا من خير فإن الله تعالى كان به\n عليمًا لا يخفى عليه شيء منه ولا من غيره",
"يسألونك أيها الرسول عن حكم ميراث الكلالة \nوهو من مات وليس له ولدٌ ولا والد قل \nالله يُبيِّن لكم الحكم فيها إن مات امرؤ\n ليس له ولد ولا والد وله أخت لأبيه وأمه\n أو لأبيه فقط فلها نصف تركته ويرث أخوها\n شقيقًا كان أو لأب جميع مالها إذا ماتت\n وليس لها ولد ولا والد فإن كان لمن\n مات كلالةً أختان فلهما الثلثان مما ترك \nوإذا اجتمع الذكور من الإخوة لغير أم مع\n الإناث فللذكر مثل نصيب الأنثيين من أخواته\n يُبيِّن الله لكم قسمة المواريث وحكم\n الكلالة لئلا تضلوا عن الحقِّ في أمر المواريث\n والله عالم بعواقب الأمور\n وما فيها من الخير لعباده"]
max = len(Quote) - 1
min = 0
opened = 0

def page1():
    if int(boy.get())!=0 and int(girl.get())==0:
        kboy=int(floss.get())/int(boy.get())
        Lmother = 0
        Lfather = 0
        Lwife1 = Lwife2 = Lwife3 = Lwife4 = 0
        Lgirl=0
        Lbrother=Lsister=0
    elif int(boy.get())!=0 and int(girl.get())!=0:
        S=int(floss.get())/(2*int(boy.get())+int(girl.get()))
        kboy=S*2
        Lgirl=S
        Lmother=0
        Lfather=0
        Lwife1=Lwife2=Lwife3=Lwife4=0
        Lbrother=Lsister=0



    elif boy.get()==0 and int(girl.get())!=0 and int(father.get())==0 and int(mother.get())==0 and int(wife.get())==0:
        Lgirl=int(floss.get())/int(girl.get())
        kboy=0
        Lbrother=Lsister=0



    elif boy.get()==0 and int(girl.get())==1 and int(father.get())!=0 and int(mother.get())!=0 and int(wife.get())==0:
        R=floss.get()/2
        T=floss.get()/6
        Lgirl=R/girl.get()
        Lmother=T
        Lfather=T
        kboy=0
    elif boy.get()==0 and int(girl.get())>1 and int(father.get())!=0 and int(mother.get())!=0 and int(wife.get())==0:
        R=floss.get()/2
        T=floss.get()/6
        Lgirl=R/girl.get()
        Lmother=T
        Lfather=T
        kboy=0
    elif boy.get()==0 and int(girl.get())>=1 and int(father.get())==0 and int(mother.get())!=0 and int(wife.get())==0:
        R=floss.get()/2
        T=floss.get()/6
        Lgirl=R/girl.get()
        Lmother=T
        Lfather=0
        kboy=0
    elif boy.get()==0 and int(girl.get())>=1 and int(father.get())!=0 and int(mother.get())==0 and int(wife.get())==0:
        R=floss.get()/2
        T=floss.get()/6
        Lgirl=R/girl.get()
        Lmother=0
        Lfather=T
        kboy=0
    elif boy.get()==0 and int(girl.get())==1 and int(father.get())==0 and int(mother.get())==0 and int(wife.get())==1:
        R=floss.get()/2
        P=floss.get()/8
        Lgirl=R
        Lwife1=P
        kboy=0
        Lwife2=Lwife3=Lwife4=0
        Lmother = 0
        Lfather = 0
    elif boy.get()==0 and int(girl.get())==1 and int(father.get())==0 and int(mother.get())==0 and int(wife.get())==2:
        R=floss.get()/2
        P=floss.get()/8
        Lgirl=R
        Lwife1=Lwife2=P
        Lwife3 = Lwife4 = 0
        kboy=0
        Lmother=0
        Lfather=0
    elif boy.get()==0 and int(girl.get())==1 and int(father.get())==0 and int(mother.get())==0 and int(wife.get())==3:
        R=floss.get()/2
        P=floss.get()/8
        Lgirl=R
        Lwife1=Lwife2=Lwife3=P
        Lwife4 = 0
        kboy=0
        Lmother = 0
        Lfather = 0

    elif boy.get()==0 and int(girl.get())==1 and int(father.get())==0 and int(mother.get())==0 and int(wife.get())==4:
        Lgirl=floss.get()/2
        Lwife1 = Lwife2 = Lwife3 = Lwife4 =floss.get()/8
        kboy=0
        Lmother = 0
        Lfather = 0


    elif boy.get() == 0 and int(girl.get()) == 1 and int(father.get())!= 0 and int(mother.get()) == 0 and int(
            wife.get()) == 1:
        R = floss.get() / 2
        P = floss.get() / 8
        D=floss.get()/6

        Lgirl = R
        Lwife1 = P
        kboy = 0
        Lwife2 = Lwife3 = Lwife4 = 0
        Lmother = 0
        Lfather = D
    elif boy.get() == 0 and int(girl.get()) == 1 and int(father.get()) == 1 and int(mother.get()) == 0 and int(
            wife.get()) == 2:
        R = floss.get() / 2
        D=floss.get()/6

        P = floss.get() / 8
        Lgirl = R
        Lwife1 = Lwife2 = P
        Lwife3 = Lwife4 = 0
        kboy = 0
        Lmother = 0
        Lfather = D
    elif boy.get() == 0 and int(girl.get()) == 1 and int(father.get()) == 1 and int(mother.get()) == 0 and int(
            wife.get()) == 3:
        R = floss.get() / 2
        P = floss.get() / 8
        D=floss.get()/6

        Lgirl = R
        Lwife1 = Lwife2 = Lwife3 = P
        Lwife4 = 0
        kboy = 0
        Lmother = 0
        Lfather = D

    elif boy.get() == 0 and int(girl.get()) == 1 and int(father.get()) == 1 and int(mother.get()) == 0 and int(
            wife.get()) == 4:
        Lgirl = floss.get() / 2
        D=floss.get()/6

        Lwife1 = Lwife2 = Lwife3 = Lwife4 = floss.get() / 8
        kboy = 0
        Lmother = 0
        Lfather = D


    elif boy.get() == 0 and int(girl.get()) == 1 and int(father.get()) != 0 and int(mother.get()) == 1 and int(
            wife.get()) == 1:
        R = floss.get() / 2
        P = floss.get() / 8
        D = floss.get() / 6

        Lgirl = R
        Lwife1 = P
        kboy = 0
        Lwife2 = Lwife3 = Lwife4 = 0
        Lmother = D
        Lfather = D
    elif boy.get() == 0 and int(girl.get()) == 1 and int(father.get()) == 1 and int(mother.get()) == 1 and int(
            wife.get()) == 2:
        R = floss.get() / 2
        D = floss.get() / 6

        P = floss.get() / 8
        Lgirl = R
        Lwife1 = Lwife2 = P
        Lwife3 = Lwife4 = 0
        kboy = 0
        Lmother = D
        Lfather = D
    elif boy.get() == 0 and int(girl.get()) == 1 and int(father.get()) == 1 and int(mother.get()) == 1 and int(
            wife.get()) == 3:
        R = floss.get() / 2
        P = floss.get() / 8
        D = floss.get() / 6

        Lgirl = R
        Lwife1 = Lwife2 = Lwife3 = P
        Lwife4 = 0
        kboy = 0
        Lmother = D
        Lfather = D

    elif boy.get() == 0 and int(girl.get()) == 1 and int(father.get()) == 1 and int(mother.get()) == 1 and int(
            wife.get()) == 4:
        Lgirl = floss.get() / 2
        D = floss.get() / 6

        Lwife1 = Lwife2 = Lwife3 = Lwife4 = floss.get() / 8
        kboy = 0
        Lmother = D
        Lfather = D


    elif boy.get()==0 and int(girl.get())==1 and int(father.get())==0 and int(mother.get())==1 and int(wife.get())==1:
        R=floss.get()/2
        P=floss.get()/8
        D=floss.get()/6
        Lgirl=R
        Lwife1=P
        kboy=0
        Lwife2=Lwife3=Lwife4=0
        Lmother = D
        Lfather = 0
    elif boy.get()==0 and int(girl.get())==1 and int(father.get())==0 and int(mother.get())==1 and int(wife.get())==2:
        R=floss.get()/2
        P=floss.get()/8
        D=floss.get()/6

        Lgirl=R
        Lwife1=Lwife2=P
        Lwife3 = Lwife4 = 0
        kboy=0
        Lmother=D
        Lfather=0
    elif boy.get()==0 and int(girl.get())==1 and int(father.get())==0 and int(mother.get())==1 and int(wife.get())==3:
        R=floss.get()/2
        P=floss.get()/8
        D=floss.get()/6

        Lgirl=R
        Lwife1=Lwife2=Lwife3=P
        Lwife4 = 0
        kboy=0
        Lmother = D
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get())  ==4 and brother.get()!= 0 and sister.get()!= 0 :
      

        Lgirl = floss.get()*0.59 /girl.get()
        Lbrother=Lsister=0

        kboy = 0
        Lwife1 = Lwife2 = Lwife3 = Lwife4 = floss.get()*0.11 /4
        Lmother= Lfather = (floss.get())*0.15
    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 3 and brother.get() != 0 and sister.get() != 0:

        Lgirl = floss.get() * 0.59 / girl.get()
        Lbrother = Lsister = 0

        kboy = 0
        Lwife4 =0
        Lwife1 = Lwife2 = Lwife3 = floss.get() * 0.11 / 3
        Lmother = Lfather = (floss.get()) * 0.15
    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 2 and brother.get() != 0 and sister.get() != 0:

        Lgirl = floss.get() * 0.59 / girl.get()
        Lbrother = Lsister = 0

        kboy = 0
        Lwife4 = Lwife3= 0
        Lwife1 = Lwife2 = floss.get() * 0.11 / 2
        Lmother = Lfather = (floss.get()) * 0.15
    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 1 and brother.get() != 0 and sister.get() != 0:

        Lgirl = floss.get() * 0.59 / girl.get()
        Lbrother = Lsister = 0

        kboy = 0
        Lwife2 =Lwife4 = Lwife3= 0
        Lwife1 =  floss.get() * 0.11 
        Lmother = Lfather = (floss.get()) * 0.15

    elif boy.get()==0 and int(girl.get())==1 and int(father.get())==0 and int(mother.get())==1 and int(wife.get())==4:
        Lgirl=floss.get()/2
        D=floss.get()/6

        Lwife1 = Lwife2 = Lwife3 = Lwife4 =floss.get()/8
        kboy=0
        Lmother = D
        Lfather = 0





    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 1:
        R = floss.get() *2/ 3
        P = floss.get() / 8
        Lgirl = R/ girl.get()
        Lwife1 = P
        kboy = 0
        Lwife2 = Lwife3 = Lwife4 = 0
        Lmother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 2:
        R = floss.get() *2/ 3
        P = floss.get() / 8
        Lgirl = R/ girl.get()
        Lwife1 = Lwife2 = P
        Lwife3 = Lwife4 = 0
        kboy = 0
        Lmother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 3:
        R = floss.get()*2 / 3
        P = floss.get() / 8
        Lgirl = R
        Lwife1 = Lwife2 = Lwife3 = P
        Lwife4 = 0
        kboy = 0
        Lmother = 0
        Lfather = 0

    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 4:
        R = floss.get()*2 / 3
        Lgirl=R
        Lwife1 = Lwife2 = Lwife3 = Lwife4 = floss.get() / 8
        kboy = 0
        Lmother = 0
        Lfather = 0


    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 1:
        R = floss.get() *2/ 3
        P = floss.get() / 8
        D = floss.get() / 6

        Lgirl = R/ girl.get()
        Lwife1 = P
        kboy = 0
        Lwife2 = Lwife3 = Lwife4 = 0
        Lmother = 0
        Lfather = D
    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 1 and int(mother.get()) == 0 and int(
            wife.get()) == 2:
        R = floss.get() *2/ 3
        D = floss.get() / 6

        P = floss.get() / 8
        Lgirl = R/ girl.get()
        Lwife1 = Lwife2 = P
        Lwife3 = Lwife4 = 0
        kboy = 0
        Lmother = 0
        Lfather = D
    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 1 and int(mother.get()) == 0 and int(
            wife.get()) == 3:
        R = floss.get()*2 / 3
        P = floss.get() / 8
        D = floss.get() / 6

        Lgirl = R/ girl.get()
        Lwife1 = Lwife2 = Lwife3 = P
        Lwife4 = 0
        kboy = 0
        Lmother = 0
        Lfather = D

    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 1 and int(mother.get()) == 0 and int(
            wife.get()) == 4:
        Lgirl = floss.get() / girl.get()
        D = floss.get() / 6

        Lwife1 = Lwife2 = Lwife3 = Lwife4 = floss.get() / 8
        kboy = 0
        Lmother = 0
        Lfather = D


    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) != 0 and int(mother.get()) == 1 and int(
            wife.get()) == 1:
        R = floss.get() *2/ 3
        P = floss.get() / 8
        D = floss.get() / 6

        Lgirl = R/ girl.get()
        Lwife1 = P
        kboy = 0
        Lwife2 = Lwife3 = Lwife4 = 0
        Lmother = D
        Lfather = D
    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 1 and int(mother.get()) == 1 and int(
            wife.get()) == 2:
        R = floss.get() *2/ 3
        D = floss.get() / 6

        P = floss.get() / 8
        Lgirl = R/ girl.get()
        Lwife1 = Lwife2 = P
        Lwife3 = Lwife4 = 0
        kboy = 0
        Lmother = D
        Lfather = D
    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 1 and int(mother.get()) == 1 and int(
            wife.get()) == 3:
        R = floss.get() *2/ 3
        P = floss.get() / 8
        D = floss.get() / 6

        Lgirl = R/ girl.get()
        Lwife1 = Lwife2 = Lwife3 = P
        Lwife4 = 0
        kboy = 0
        Lmother = D
        Lfather = D

    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 1 and int(mother.get()) == 1 and int(
            wife.get()) == 4:
        Lgirl = (floss.get() *2/ 3)/ girl.get()
        D = floss.get() / 6

        Lwife1 = Lwife2 = Lwife3 = Lwife4 = floss.get() / 8
        kboy = 0
        Lmother = D
        Lfather = D


    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 0 and int(mother.get()) == 1 and int(
            wife.get()) == 1:
        R = floss.get() *2/ 3
        P = floss.get() / 8
        D = floss.get() / 6
        Lgirl = R/ girl.get()
        Lwife1 = P
        kboy = 0
        Lwife2 = Lwife3 = Lwife4 = 0
        Lmother = D
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 0 and int(mother.get()) == 1 and int(
            wife.get()) == 2:
        R = floss.get() *2/ 3
        P = floss.get() / 8
        D = floss.get() / 6

        Lgirl = R/ girl.get()
        Lwife1 = Lwife2 = P
        Lwife3 = Lwife4 = 0
        kboy = 0
        Lmother = D
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) >= 1 and int(father.get()) == 0 and int(mother.get()) == 1 and int(
            wife.get()) == 3:
        R = floss.get() *2/ 3
        P = floss.get() / 8
        D = floss.get() / 6

        Lgirl = R/ girl.get()
        Lwife1 = Lwife2 = Lwife3 = P
        Lwife4 = 0
        kboy = 0
        Lmother = D
        Lfather = 0

    elif boy.get() ==0 and int(girl.get()) >=1 and int(father.get()) == 0 and int(mother.get()) == 1 and int(
            wife.get()) == 4:
        Lgirl = (floss.get() *2/ 3)/ girl.get()
        D = floss.get() / 6

        Lwife1 = Lwife2 = Lwife3 = Lwife4 = floss.get() / 8
        kboy = 0
        Lmother = D
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 0 and int(sister.get())!=0 and int(brother.get())!=0:
        R = floss.get()/ 9
        Lgirl=0
        Lwife1 = Lwife2 = Lwife3 = Lwife4 = 0
        kboy = 0
        Lmother = floss.get()/6
        Lsister=R/sister.get()
        Lbrother=2*R/brother.get()
        Lfather = floss.get()-Lbrother-Lsister-Lmother

    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 1 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife1 =floss.get()/ 8
        Lwife2 = Lwife3 = Lwife4 = 0
        kboy = 0
        Lmother = floss.get() / 6
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather = floss.get() - Lbrother - Lsister - Lmother-Lwife1
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 2 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife2 = Lwife1 = floss.get() / 8
        Lwife3 = Lwife4 = 0
        kboy = 0
        Lmother = floss.get() / 6
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather = floss.get() - Lbrother - Lsister - Lmother - Lwife1-Lwife2
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 3 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife3 =Lwife2 = Lwife1 = floss.get() / 8
        Lwife4 = 0
        kboy = 0
        Lmother = floss.get() / 6
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather = floss.get() - Lbrother - Lsister - Lmother - Lwife1 - Lwife2-Lwife3
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 4 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife4 =Lwife3 = Lwife2 = Lwife1 = floss.get() / 8

        kboy = 0
        Lmother = floss.get() / 6
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather = floss.get() - Lbrother - Lsister - Lmother - Lwife1 - Lwife2 - Lwife3-Lwife4
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) != 0 and int(
            wife.get()) == 0 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife4 = Lwife3 = Lwife2 = Lwife1 = 0

        kboy = 0
        Lfather = 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lmother = floss.get() - Lbrother - Lsister  - Lwife1 - Lwife2 - Lwife3 - Lwife4
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) != 0 and int(
            wife.get()) == 1 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife4 = Lwife3 = Lwife2 = 0
        Lwife1 = floss.get()/8

        kboy = 0
        Lfather = 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lmother = floss.get() - Lbrother - Lsister - Lwife1 - Lwife2 - Lwife3 - Lwife4
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) != 0 and int(
            wife.get()) == 2 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife4 = Lwife3 =  0
        Lwife2 =Lwife1 = floss.get()/8

        kboy = 0
        Lfather = 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lmother = floss.get() - Lbrother - Lsister - Lwife1 - Lwife2 - Lwife3 - Lwife4
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) != 0 and int(
            wife.get()) == 3 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife4 =  0
        Lwife3 =Lwife2 =Lwife1 = floss.get()/8

        kboy = 0
        Lfather = 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lmother = floss.get() - Lbrother - Lsister - Lwife1 - Lwife2 - Lwife3 - Lwife4
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) != 0 and int(
            wife.get()) == 4 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife4 =Lwife3 =Lwife2 =Lwife1 = floss.get()/8

        kboy = 0
        Lfather = 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lmother = floss.get() - Lbrother - Lsister - Lwife1 - Lwife2 - Lwife3 - Lwife4

    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) ==0 and int(
            wife.get()) == 0 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife4 = Lwife3 = Lwife2 = Lwife1 = 0

        kboy = 0
        Lmother= 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather = floss.get() - Lbrother - Lsister  - Lwife1 - Lwife2 - Lwife3 - Lwife4
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) !=  0 and int(mother.get()) == 0 and int(
            wife.get()) == 1 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife4 = Lwife3 = Lwife2 = 0
        Lwife1 = floss.get()/8

        kboy = 0
        Lmother= 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather = floss.get() - Lbrother - Lsister - Lwife1 - Lwife2 - Lwife3 - Lwife4
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) !=  0 and int(mother.get()) == 0 and int(
            wife.get()) == 2 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife4 = Lwife3 =  0
        Lwife2 =Lwife1 = floss.get()/8

        kboy = 0
        Lmother = 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather = floss.get() - Lbrother - Lsister - Lwife1 - Lwife2 - Lwife3 - Lwife4
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) !=  0 and int(mother.get()) == 0 and int(
            wife.get()) == 3 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife4 =  0
        Lwife3 =Lwife2 =Lwife1 = floss.get()/8

        kboy = 0
        Lmother = 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather= floss.get() - Lbrother - Lsister - Lwife1 - Lwife2 - Lwife3 - Lwife4
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) !=  0 and int(mother.get()) ==0 and int(
            wife.get()) == 4 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / 9
        Lgirl = 0
        Lwife4 =Lwife3 =Lwife2 =Lwife1 = floss.get()/8

        kboy = 0
        Lmother = 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather = floss.get() - Lbrother - Lsister - Lwife1 - Lwife2 - Lwife3 - Lwife4

    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) ==0 and int(
            wife.get()) == 0 and int(sister.get()) != 0 and int(brother.get()) != 0:
        R = floss.get() / (2*brother.get()+sister.get())
        Lgirl = 0
        Lwife4 = Lwife3 = Lwife2 = Lwife1 = 0

        kboy = 0
        Lmother= Lfather=0
        Lsister = R
        Lbrother = 2 * R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) ==  0 and int(mother.get()) == 0 and int(
            wife.get()) == 1 and int(sister.get()) != 0 and int(brother.get()) != 0:
        Lwife1 = floss.get() / 8

        R = (floss.get() -Lwife1)/3
        Lgirl = 0
        Lwife4 = Lwife3 = Lwife2 = 0

        kboy = 0
        Lmother= 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) ==0  and int(mother.get()) == 0 and int(
            wife.get()) == 2 and int(sister.get()) != 0 and int(brother.get()) != 0:
        Lwife4 = Lwife3 = 0
        Lwife2 = Lwife1 = floss.get() / 8
        R = (floss.get() -Lwife1-Lwife2)/3
        Lgirl = 0


        kboy = 0
        Lmother = 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) ==  0 and int(mother.get()) == 0 and int(
            wife.get()) == 3 and int(sister.get()) != 0 and int(brother.get()) != 0:
        Lwife3 =Lwife2 =Lwife1 = floss.get()/8

        R = (floss.get() -Lwife1-Lwife2-Lwife3)/3
        Lgirl = 0
        Lwife4 =  0
        Lwife3 =Lwife2 =Lwife1 = floss.get()/8

        kboy = 0
        Lmother = 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather= 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) ==  0 and int(mother.get()) ==0 and int(
            wife.get()) == 4 and int(sister.get()) != 0 and int(brother.get()) != 0:
        Lwife4 =Lwife3 =Lwife2 =Lwife1 = floss.get()/8

        R = (floss.get() -Lwife1-Lwife2-Lwife3-Lwife4)/3
        Lgirl = 0

        kboy = 0
        Lmother = 0
        Lsister = R / sister.get()
        Lbrother = 2 * R / brother.get()
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 0 and int(sister.get()) == 0 and int(brother.get()) == 0:
        Lwife4 = Lwife3 = Lwife2 = Lwife1 = 0

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4) / 3
        Lgirl = 0

        kboy = 0
        Lmother = floss.get()/3
        Lsister = 0
        Lbrother = 0
        Lfather = floss.get()*2/3
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 1 and int(sister.get()) == 0 and int(brother.get()) == 0:
        Lwife4 = Lwife3 = Lwife2  = 0
        Lwife1 =floss.get()/8
        Lmother = floss.get()/3

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4-Lmother)
        Lgirl = 0

        kboy = 0
        Lmother = floss.get()/3
        Lsister = 0
        Lbrother = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 2 and int(sister.get()) == 0 and int(brother.get()) == 0:
        Lwife4 = Lwife3 =  0
        Lwife2  =Lwife1 =floss.get()/8
        Lmother = floss.get()/3

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4-Lmother)
        Lgirl = 0

        kboy = 0
        Lmother = floss.get()/3
        Lsister = 0
        Lbrother = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 3 and int(sister.get()) == 0 and int(brother.get()) == 0:
        Lwife4 =   0
        Lwife3 =Lwife2  =Lwife1 =floss.get()/8
        Lmother = floss.get()/3

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4-Lmother)
        Lgirl = 0

        kboy = 0
        Lmother = floss.get()/3
        Lsister = 0
        Lbrother = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) != 0 and int(
            wife.get()) == 4 and int(sister.get()) == 0 and int(brother.get()) == 0:

        Lwife4 =Lwife3 =Lwife2  =Lwife1 =floss.get()/8
        Lmother = floss.get()/3

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4-Lmother)
        Lgirl = 0

        kboy = 0
        Lmother = floss.get()/3
        Lsister = 0
        Lbrother = 0
        Lfather = R

    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 0 and int(sister.get()) == 0 and int(brother.get()) == 0:
        Lwife4 = Lwife3 = Lwife2 = Lwife1 = 0

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4)
        Lgirl = 0

        kboy = 0
        Lmother = 0
        Lsister = 0
        Lbrother = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 1 and int(sister.get()) == 0 and int(brother.get()) == 0:
        Lwife4 = Lwife3 = Lwife2 = 0
        Lwife1 = floss.get() / 8
        Lmother =0


        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4 - Lmother)
        Lgirl = 0

        kboy = 0
        Lsister = 0
        Lbrother = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 2 and int(sister.get()) == 0 and int(brother.get()) == 0:
        Lwife4 = Lwife3 = 0
        Lwife2 = Lwife1 = floss.get() / 8
        Lmother = 0

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4 - Lmother)
        Lgirl = 0

        kboy = 0

        Lsister = 0
        Lbrother = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 3 and int(sister.get()) == 0 and int(brother.get()) == 0:
        Lwife4 = 0
        Lwife3 = Lwife2 = Lwife1 = floss.get() / 8
        Lmother = 0

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4 - Lmother)
        Lgirl = 0

        kboy = 0
        Lsister = 0
        Lbrother = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 4 and int(sister.get()) == 0 and int(brother.get()) == 0:

        Lwife4 = Lwife3 = Lwife2 = Lwife1 = floss.get() / 8
        Lmother = 0

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4 - Lmother)
        Lgirl = 0

        kboy = 0
        Lsister = 0
        Lbrother = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) != 0 and int(
            wife.get()) == 0 and int(sister.get()) == 0 and int(brother.get()) == 0:

        Lwife4 = Lwife3 = Lwife2 = Lwife1 = 0

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4 )
        Lgirl = 0
        Lmother = R

        kboy = 0
        Lsister = 0
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) != 0 and int(
            wife.get()) == 1 and int(sister.get()) == 0 and int(brother.get()) == 0:

        Lwife4 = Lwife3 = Lwife2 =0
        Lwife1 = floss.get()/8

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4 )
        Lgirl = 0
        Lmother = R

        kboy = 0
        Lsister = 0
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) != 0 and int(
            wife.get()) == 2 and int(sister.get()) == 0 and int(brother.get()) == 0:

        Lwife4 = Lwife3 =  0
        Lwife2 =Lwife1 = floss.get() / 8

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4)
        Lgirl = 0
        Lmother = R

        kboy = 0
        Lsister = 0
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) != 0 and int(
            wife.get()) == 3 and int(sister.get()) == 0 and int(brother.get()) == 0:

        Lwife4 = 0
        Lwife3 = Lwife2 = Lwife1 = floss.get() / 8

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4)
        Lgirl = 0
        Lmother = R

        kboy = 0
        Lsister = 0
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) != 0 and int(
            wife.get()) == 4 and int(sister.get()) == 0 and int(brother.get()) == 0:

        Lwife4 =  Lwife3 = Lwife2 = Lwife1 = floss.get() / 8

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4)
        Lgirl = 0
        Lmother = R

        kboy = 0
        Lsister = 0
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 0 and int(sister.get()) == 0 and int(brother.get()) != 0:

        Lwife4 = Lwife3 = Lwife2 = Lwife1 = 0

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4)
        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = 0
        Lbrother = R/ brother.get()
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 0 and int(sister.get()) != 0 and int(brother.get()) == 0:

        Lwife4 = Lwife3 = Lwife2 = Lwife1=0

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4)
        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = R/ sister.get()
        Lbrother = 0
        Lfather = 0

    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 1 and int(sister.get()) == 0 and int(brother.get()) != 0:

        Lwife4 = Lwife3 = Lwife2 =0
        Lwife1 = floss.get()/8

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4 )
        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = 0
        Lbrother = R/ brother.get()
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 2 and int(sister.get()) == 0 and int(brother.get()) != 0:

        Lwife4 = Lwife3 =  0
        Lwife2 =Lwife1 = floss.get() / 8

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4)
        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = 0
        Lbrother = R/ brother.get()
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 3 and int(sister.get()) == 0 and int(brother.get()) != 0:

        Lwife4 = 0
        Lwife3 = Lwife2 = Lwife1 = floss.get() / 8

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4)
        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = 0
        Lbrother = R/ brother.get()
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 4 and int(sister.get()) == 0 and int(brother.get()) != 0:

        Lwife4 =  Lwife3 = Lwife2 = Lwife1 = floss.get() / 8

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4)
        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = 0
        Lbrother = R/ brother.get()
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 1 and int(sister.get()) != 0 and int(brother.get()) == 0:

        Lwife4 = Lwife3 = Lwife2 =0
        Lwife1 = floss.get()/8

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4 )
        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = R/ sister.get()
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 2 and int(sister.get()) != 0 and int(brother.get()) == 0:

        Lwife4 = Lwife3 =  0
        Lwife2 =Lwife1 = floss.get() / 8

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4)
        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = R/ sister.get()
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 3 and int(sister.get()) != 0 and int(brother.get()) == 0:

        Lwife4 = 0
        Lwife3 = Lwife2 = Lwife1 = floss.get() / 8

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4)
        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = R/ sister.get()
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 4 and int(sister.get()) != 0 and int(brother.get()) == 0:

        Lwife4 =  Lwife3 = Lwife2 = Lwife1 = floss.get() / 8

        R = (floss.get() - Lwife1 - Lwife2 - Lwife3 - Lwife4)
        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = R/ sister.get()
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 1 and int(sister.get()) == 0 and int(brother.get()) == 0:

        Lwife4 =  Lwife3 = Lwife2 = 0
        Lwife1 = floss.get() / 4

        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = 0
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 2 and int(sister.get()) == 0 and int(brother.get()) == 0:

        Lwife4 = Lwife3 = 0
        Lwife2 =Lwife1 = floss.get() / 8

        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = 0
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 3 and int(sister.get()) == 0 and int(brother.get()) == 0:

        Lwife4 = 0
        Lwife3 = Lwife2 =Lwife1 = floss.get() / 12

        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = 0
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 4 and int(sister.get()) == 0 and int(brother.get()) == 0:

        Lwife4 =  Lwife3 = Lwife2 =Lwife1 = floss.get() / 16

        Lgirl = 0
        Lmother = 0

        kboy = 0
        Lsister = 0
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 0 and int(sister.get()) == 0 and int(brother.get()) != 0:

        Lwife4 =  Lwife3 = Lwife2 =Lwife1 = 0

        Lgirl = 0
        Lmother = 0
        Lbrother = floss.get()/6*brother.get()

        R=floss.get()-Lbrother
        kboy = 0
        Lsister = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 1 and int(sister.get()) == 0 and int(brother.get()) != 0:

        Lwife4 =  Lwife3 = Lwife2 =0
        Lwife1 = floss.get()/9

        Lgirl = 0
        Lmother = 0
        Lbrother = floss.get()/6*brother.get()

        R=floss.get()-Lbrother- Lwife4 - Lwife3 -Lwife2 -Lwife1
        kboy = 0
        Lsister = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 2 and int(sister.get()) == 0 and int(brother.get()) != 0:

        Lwife4 =  Lwife3 = 0
        Lwife2 =Lwife1 = floss.get()/9

        Lgirl = 0
        Lmother = 0
        Lbrother = floss.get()/6*brother.get()

        R=floss.get()-Lbrother- Lwife4 -Lwife3 -Lwife2 -Lwife1
        kboy = 0
        Lsister = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 3 and int(sister.get()) == 0 and int(brother.get()) != 0:

        Lwife4 =   0
        Lwife3 =Lwife2 =Lwife1 = floss.get()/9

        Lgirl = 0
        Lmother = 0
        Lbrother = floss.get()/6*brother.get()

        R=floss.get()-Lbrother- Lwife4 - Lwife3 -Lwife2 -Lwife1
        kboy = 0
        Lsister = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 4 and int(sister.get()) == 0 and int(brother.get()) != 0:

        Lwife4 = Lwife3 =Lwife2 =Lwife1 = floss.get()/9

        Lgirl = 0
        Lmother = 0
        Lbrother = floss.get()/6*brother.get()

        R=floss.get()-Lbrother- Lwife4 -Lwife3 -Lwife2 -Lwife1
        kboy = 0
        Lsister = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 1 and int(sister.get()) != 0 and int(brother.get()) == 0:

        Lwife4 =  Lwife3 = Lwife2 =0
        Lwife1 = floss.get()/9

        Lgirl = 0
        Lmother = 0
        Lsister = floss.get()/6*sister.get()

        R=floss.get()-Lsister- Lwife4 - Lwife3 -Lwife2 -Lwife1
        kboy = 0
        Lbrother = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 2 and int(sister.get()) != 0 and int(brother.get()) == 0:

        Lwife4 =  Lwife3 = 0
        Lwife2 =Lwife1 = floss.get()/9

        Lgirl = 0
        Lmother = 0
        Lsister = floss.get()/6*sister.get()

        R=floss.get()-Lsister- Lwife4 -Lwife3 -Lwife2 -Lwife1
        kboy = 0
        Lbrother = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 3 and int(sister.get()) != 0 and int(brother.get()) == 0:

        Lwife4 =   0
        Lwife3 =Lwife2 =Lwife1 = floss.get()/9

        Lgirl = 0
        Lmother = 0
        Lsister = floss.get()/6*sister.get()

        R=floss.get()-Lsister- Lwife4 - Lwife3 -Lwife2 -Lwife1
        kboy = 0
        Lbrother = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 4 and int(sister.get()) != 0 and int(brother.get()) == 0:

        Lwife4 = Lwife3 =Lwife2 =Lwife1 = floss.get()/9

        Lgirl = 0
        Lmother = 0
        Lsister = floss.get()/6*sister.get()

        R=floss.get()-Lsister- Lwife4 -Lwife3 -Lwife2 -Lwife1
        kboy = 0
        Lbrother = 0
        Lfather = R
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) != 0 and int(
            wife.get()) == 0 and int(sister.get()) != 0 and int(brother.get()) == 0:
        Lsister = floss.get()/6*sister.get()

        Lwife4 = Lwife3 =Lwife2 =Lwife1 = 0
        R=floss.get()-Lsister- Lwife4 -Lwife3 -Lwife2 -Lwife1

        Lgirl = 0
        Lmother = R

        kboy = 0
        Lbrother = 0
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) == 0 and int(mother.get()) != 0 and int(
            wife.get()) == 0 and int(sister.get()) == 0 and int(brother.get()) != 0:
        Lbrother = floss.get()/6*brother.get()

        Lwife4 = Lwife3 =Lwife2 =Lwife1 = 0
        R=floss.get()-Lbrother- Lwife4 -Lwife3 -Lwife2 -Lwife1

        Lgirl = 0
        Lmother = R

        kboy = 0
        Lbrother = R
        Lfather = 0
    elif boy.get() == 0 and int(girl.get()) != 0 and int(father.get()) == 0 and int(mother.get()) == 0 and int(
            wife.get()) == 0 and int(sister.get()) != 0 and int(brother.get()) == 0:


        Lwife4 = Lwife3 = Lwife2 = Lwife1 = 0
        R = floss.get() /2

        Lgirl = R/girl.get()
        Lsister = R/sister.get()

        Lmother = 0

        kboy = 0
        Lbrother = 0
        Lfather = 0
   
    elif boy.get() == 0 and int(girl.get()) == 0 and int(father.get()) != 0 and int(mother.get()) == 0 and int(
            wife.get()) == 0 and int(sister.get()) != 0 and int(brother.get()) == 0:


        Lwife4 = Lwife3 = Lwife2 = Lwife1 = 0
        R = floss.get() /3

        Lgirl =0
        Lsister = R/sister.get()

        Lmother = 0

        kboy = 0
        Lbrother = 0
        Lfather = floss.get()-R


    else:
        kboy=0
        Lgirl=Lbrother=Lsister=Lfather=Lmother=Lwife1=Lwife2=Lwife3=Lwife4=0



    global ws1

    ws.destroy()
    ws1 = Tk()
    ws1.title('الإرث')

    ws1.geometry('1300x700')
    ws1.config(bg='yellow')
    canvas = Canvas(ws1, height=700, width=1300)
    canvas.pack()


    image = PhotoImage(file='SA.png')
    canvas.create_image(0, 0, image=image, anchor=NW)
    frame = Frame(canvas, bg="#335379")
    frame.place(x=200, y=100)


    arrow3 = PhotoImage(file="arrow3.png")
    Button(canvas,image=arrow3,command=go_back2,bg="white",activebackground="white").place(x=0,y=0,anchor=NW)
    Label(frame, text=" قسمة التركة    ", font=('Arial', 28), fg="white", bg="#335379").grid(row=0, column=1,columnspan=4)
    Label(frame, text=" نصيب الأبناء    ", font=('Arial', 20), fg="white", bg="#335379").grid(row=1, column=4)
    Label(frame, text="  نصيب البنات   ", font=('Arial', 20), fg="white", bg="#335379").grid(row=1, column=3)
    Label(frame, text="  نصيب الأم   ", font=('Arial', 20), fg="white", bg="#335379").grid(row=1, column=2)
    Label(frame, text="  نصيب الأب   ", font=('Arial', 20), fg="white", bg="#335379").grid(row=1, column=1)

    label1=Label(frame, text=kboy, font=('arial', 20,"bold"), fg="white", bg="#335379")
    label1.grid(row=2, column=4)
    label2 = Label(frame, text=Lgirl, font=('arial', 20,"bold"), fg="white", bg="#335379")
    label2.grid(row=2, column=3)
    label3 = Label(frame, text=Lmother, font=('arial', 20,"bold"), fg="white", bg="#335379")
    label3.grid(row=2, column=2)
    label4 = Label(frame, text=Lfather, font=('arial', 20,"bold"), fg="white", bg="#335379")
    label4.grid(row=2, column=1)
    Label(frame, text=" نصيب الزوجة الأولى    ", font=('Aeial', 20), fg="white", bg="#335379").grid(row=3, column=4)
    Label(frame, text="  نصيب الزوجة الثانية   ", font=('Aeial', 20), fg="white", bg="#335379").grid(row=3, column=3)
    Label(frame, text="  نصيب الزوجة الثالثة   ", font=('Aeial', 20), fg="white", bg="#335379").grid(row=3, column=2)
    Label(frame, text="  نصيب الزوجة الرابعة   ", font=('Aeial', 20), fg="white", bg="#335379").grid(row=3, column=1)
    label5 = Label(frame, text=Lwife4, font=('Aeial', 20), fg="white", bg="#335379")
    label5.grid(row=4, column=1)
    label6 = Label(frame, text=Lwife3, font=('arial', 20,"bold"), fg="white", bg="#335379")
    label6.grid(row=4, column=2)
    label7 = Label(frame, text=Lwife2, font=('arial', 20,"bold"), fg="white", bg="#335379")
    label7.grid(row=4, column=3)
    label8 = Label(frame, text=Lwife1, font=('arial', 20,"bold"), fg="white", bg="#335379")
    label8.grid(row=4, column=4)
    Label(frame, text=" نصيب الإخوة    ", font=('arial', 20,"bold"), fg="white", bg="#335379").grid(row=5, column=1,columnspan=2)
    Label(frame, text="  نصيب الأخوات   ", font=('arial', 20,"bold"), fg="white", bg="#335379").grid(row=5, column=3,columnspan=2)
    label9 = Label(frame, text=Lbrother, font=('arial', 20,"bold"), fg="white", bg="#335379")
    label9.grid(row=6, column=1,columnspan=2)
    label10 = Label(frame, text=Lsister, font=('arial', 20,"bold"), fg="white", bg="#335379")
    label10.grid(row=6, column=3,columnspan=2)
    ws1.mainloop() 

def config():
  global text_area
  global page_number_label
  global window
  
  window = Tk()
  window.geometry("800x450+230+90")
  my_background = PhotoImage(file="background2.png")
  Label(window,image=my_background).place(x=0,y=0)
  text_area = Label(window,width=31,height=8,bg='light yellow',text=Quote[page_num],font=("arial",28,"bold"))
  text_area.place(x=43,y=40)
  window.resizable(False, False)
  window.title("آيات عن الإرث")
  frame = Frame(window,bg="#e39042")
  frame.place(x=320,y=400)
  arrow = PhotoImage(file="arrow.png")
  arrow2 = PhotoImage(file="arrow2.png")
  Button(frame,image=arrow,bg="#e39042",activebackground="#e39042",command=next).grid(row=0,column=2)
  page_number_label =Label(frame,text=page_num+1,font=("arial",15,"bold"),padx=10,bg="#e39042")
  page_number_label.grid(row=0,column=1)
  Button(frame,image=arrow2,bg="#e39042",activebackground="#e39042",command=previous).grid(row=0,column=0)
  Button(window,text="شرح",font=("arial",15,"bold"),command=explaine,padx=5,pady=2,bg="#f69257",fg="#f7f4c3",activebackground="#f69257",activeforeground="#f7f4c3").place(x=3,y=405)
  arrow3 = PhotoImage(file="arrow3.png")
  Button(window,image=arrow3,command=go_back,bg="#b8bf6f",activebackground="#b8bf6f").place(x=0,y=0,anchor=NW)
  window.mainloop()

      
        
def heritage():
  global ws
  global floss
  global father
  global mother
  global sister
  global brother
  global boy
  global girl
  global wife 
  
  ws = Tk()
  ws.title('الإرث')

  ws.geometry('1300x700')
  ws.config(bg='yellow')
  canvas=Canvas(ws,height=700,width=1300)
  canvas.pack()

  img = PhotoImage(file='QA.png')
  canvas.create_image(0,0,image=img,anchor=NW)
  canvas.create_text(700,70,text="               المرجو ادخال معلومات الورثة        \n يقول الله تعالى: ﴿لِلرِّجَالِ ‌نَصِيبٌ مِمَّا اكْتَسَبُوا وَلِلنِّسَاءِ نَصِيبٌ مِمَّا اكْتَسَب}َْ \n           قال تعالى: {لِلذَّكَرِ مِثْلُ حَظِّ الأُنثَيَيْنِ}       ",font=('Aeial',18),fill="#62dcf6")

  frame=Frame(canvas,bg="#335379")
  frame.place(x=500,y=140)
  arrow3 = PhotoImage(file="arrow3.png")
  Button(canvas,image=arrow3,command=go_back1,bg="white",activebackground="white").place(x=0,y=0,anchor=NW)
  Label(frame,text=" : قيمة التركة    ",font=('Aeial',20),fg="white",bg="#335379").grid(row=0, column=1)
  floss=IntVar()
  entry=Entry(frame,textvariable=floss,width=22)
  entry.grid(row=0,column=0)
  Label(frame,text=" :   عدد الأبناء  ",font=('Aeial',20),fg="white",bg="#335379").grid(row=1, column=1)
  boy = IntVar()
  spin_box = Spinbox(frame,from_=0,to=24,textvariable=boy,wrap=True).grid(row=1,column=0)
  Label(frame,text=" :   عدد البنات  ",font=('Aeial',20),fg="white",bg="#335379").grid(row=2, column=1)
  girl = IntVar()
  spin_box = Spinbox(frame,from_=0,to=24,textvariable=girl,wrap=True).grid(row=2,column=0)

  Label(frame,text=" :         الأب  ",font=('Aeial',20),fg="white",bg="#335379").grid(row=3, column=1)
  father=IntVar()
  spin_box = Spinbox(frame,from_=0,to=1,textvariable=father,wrap=True).grid(row=3,column=0)


  Label(frame,text=" :          الأم  ",font=('Aeial',20),fg="white",bg="#335379").grid(row=4, column=1)
  mother=IntVar()
  spin_box = Spinbox(frame,from_=0,to=1,textvariable=mother,wrap=True).grid(row=4,column=0)


  Label(frame,text=" :  عدد الإخوة  ",font=('Aeial',20),fg="white",bg="#335379").grid(row=5, column=1)
  brother= IntVar()
  spin_box= Spinbox(frame,from_=0,to=24,textvariable=brother,wrap=True).grid(row=5,column=0)
  Label(frame,text=" :عدد الأخوات  ",font=('Aeial',20),fg="white",bg="#335379").grid(row=6, column=1)
  sister= IntVar()
  spin_box = Spinbox(frame,from_=0,to=24,textvariabl=sister,wrap=True).grid(row=6,column=0)
  Label(frame,text=" :عدد الزوجات  ",font=('Aeial',20),fg="white",bg="#335379").grid(row=7, column=1)
  wife= IntVar()
  spin_box = Spinbox(frame,from_=0,to=4,textvariable=wife,wrap=True).grid(row=7,column=0)



  button = Button(frame, text='حساب الميراث ',relief=RAISED,font=('Arial Bold', 20),command=page1)
  button.grid(row=8,column=0,columnspan=2)
  ws.mainloop()


def function():
    if x.get() == 0:
      win.destroy()
      config()        

    else:
        win.destroy()
        heritage()


def next():
  global page_num
  global opened

  if opened == 1:
    window2.destroy()
    opened =0
  window.geometry("800x450+230+90")
  page_num = page_num + 1
  if page_num > max:
    page_num = min
  text_area.config(text=Quote[page_num])
  page_number_label.config(text=page_num+1)

def previous():
  global page_num 
  global opened
  
  if opened == 1:
    window2.destroy()
    opened =0
  window.geometry("800x450+230+90")
  page_num = page_num - 1
  if page_num < min:
    page_num = max 
  text_area.config(text=Quote[page_num])
  page_number_label.config(text=page_num+1)

def explaine():
  global window2
  global opened

  window.geometry("800x450+450+90")
  window2 =Tk()
  opened = 1
  window2.resizable(False,False)
  if definition[page_num].count("\n") >= 14 :
    Y = "650"
    W = 0
  else :
    Y = "450"
    W = 80
  window2.geometry("380x{}+50+{}".format(Y,W))
  window2.title("التفسير")
  window2.config(bg="black")
  if definition[page_num].count("\n")+2 >= 15:
    text_area2 = Label(window2,width=25,height=definition[page_num].count("\n")+2,text=definition[page_num],fg="white",bg='black',font=("arial",19," bold"))
  else :
    text_area2 = Label(window2,width=25,height=15,text=definition[page_num],fg="white",bg='black',font=("arial",19," bold"))
  
  text_area2.place(x=0,y=0,anchor=NW)
  window2.mainloop()

def go_back():
  global opened

  window.destroy()
  if opened == 1:
    window2.destroy()
    opened =0
  main()

def go_back1():
    ws.destroy()
    main()

def go_back2():
    ws1.destroy()
    heritage()

def main():
  global x
  global win

  win = Tk() 
  win.geometry("710x410+250+100")
  win.resizable(False,False)
  win.title("الإرث")
  win_icon = PhotoImage(file="Page_icon.png")
  win.iconphoto(True,win_icon)

  canvas = Canvas(win,height=400,width=700)
  canvas.pack()
  background_photo = PhotoImage(file="background1.png")
  canvas.create_image(0,0,image =background_photo,anchor=NW)
  canvas.create_text(550,150,text="بكم مرحبا",font=("Verdana", 50),fill="#d5e1df")
  canvas.create_text(550,210,text=" لَا يَأْخُذُ أَحَدٌ شِبْرًا مِنَ الأرْضِ بِغَيْرِ حَقِّهِ\nإِلَّا طَوَّقَهُ اللَّهُ إلى سَبْعِ أَرَضِينَ يَومَ القِيَامَةِ",font=("Bold", 10),fill="#d5e1df")
  x= IntVar()
  frame = Frame(canvas,bg="#002f29")
  frame.place(x="350",y="340")

  for i in range(len(Topics)) :
     radio_button = Radiobutton(frame,variable=x,value=i,padx=2,text=Topics[i],command=function,font=("Impact",11),fg="#e6e2d3",bg="#002f29")
     radio_button.pack()
  copy_right_label = Label(canvas,text="© Rida nait el mouden \n     & Mouzoune mustapha",bg="#3e4444",fg="#e6e2d3")
  copy_right_label.place(x="550",y="360")

  win.mainloop()
main()


