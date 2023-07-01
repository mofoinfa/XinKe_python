import pdfplumber
import re


def get_pdf():
    """获取pdf的数据"""
    sum_text = ''
    local = 'D:/pycharm/python/项目/python培训/兼职测试/测试问答/'
    with pdfplumber.open(local + "a.pdf") as pdf:
        num_pages = len(pdf.pages)
        for page_num in range(num_pages):
            page = pdf.pages[page_num]
            text = page.extract_text()
            sum_text += text
        sum_text = sum_text.replace('\n', '')
        data = sum_text.split('.')
        del data[0]
        return data


def issue_one(data):
    """
    问题：
    以下哪一条更可能是作者所创办公司的使命？请简述原因
    1）激发创造 丰富生活
    2） 用科技让复杂的世界更简单
    3） 帮大家吃得更好，生活更好
    4） 让全球多一点幸福
    :return:
    """

    cre_num = []
    prefer_num = []
    science_num = []
    family_num = []
    for i in data:
        # 从问题的理性和感性划分（问题中1，2偏理性，3，4偏感性）
        if '我' in i and ('理解' in i or '观点' in i):  # 以作者的感概综合分析作者的观点
            # 如此分析下作者的观点更偏理性，所以判断1，2的概率偏大
            # print(i)
            pass
        # 从每个问题的关键字检索出作者更偏向的方向
        if '创造' in i:
            cre_num.append(i)
        if '科技' in i or '高能' in i or '未来' in i:
            science_num.append(i)
        if '朋友' in i or '家人' in i or '父亲' in i or '母亲' in i:
            family_num.append(i)
        if ('好' in i or '全球' in i):
            prefer_num.append(i)
    answer = '从上述的分析数据得到，作者从感性和理性的方面，更偏向于理性，也就表示更偏向于第一和第二个答案\n' \
             '从四个问题方向检索文档，发现作者对于创造和公司的关联更加紧密。综上我认为（2）更有可能是公司\n' \
             '创办的使命'
    return answer


def issue_two(data):
    """
    作者的内容截止到2016年，请根据你的理解，推测在2023年，作者的公司可
    能在从事的业务，发展情况等
    :return:
    """
    for i in data:
        if '公司' in i:
            # print(i)
            pass
    answer = '综上所述可知，作者大部分围绕这创业公司的这个角度去出发，因此可推断当时出去刚刚的创业时期，\n' \
             '在公司的发展阶段的笔记中可以总结出作者喜欢创新，并且更加关注于未来领域的发展，其中在检索中\n' \
             '的数据中提到了手机、ai等关键词。由此我推断公司可能从事ai或互联网的发展工作，在未来通过创新\n' \
             '可以开辟ai领域之前未出现的新的领域。'
    return answer
    #


def issue_three(data):
    """
    请尝试用MBTI人格分析法来分析作者的人格，并给出较详细的理由
    :param data:
    :return:
    """
    """ 精力支配：外向 E — 内向 I 
        认识世界：实感 S — 直觉 N 
        判断事物：思维 T — 情感 F 
        生活态度：判断 J — 知觉 P 
        MBTI人格分析法使用16种人格来归纳一个人的人格，依次我们从四个角度调用数据分析作者人格
    """
    future = []
    now = []
    for i in data:
        # 内向-外向：我认为的关键点在于沟通（外向）
        if '沟通' in i or '讨论' in i:
            # print(i)
            pass
        # 如上信息可得作者在笔记中多数围绕着沟通和交流来发言，以上作者第一环节更加偏外向（直觉）

        # 实感-直觉：实感是基于此物体往更加深层次去考虑，而直觉则是直面这个物体。从而我认为其中差异在于看的有多远
        if '未来' in i:
            future.append(i)
        if '现在' in i:
            now.append(i)

        # 思维 T — 情感 F：思维和情感若是从另外一个角度就是感性和理性的角度去思考问题，
        # 其中问题一的检测中显示作者更偏向于理性（思维）

        # 生活态度：判断 J — 知觉 P：判断型的人，目标很明确，他们做事果断，充满计划，会避免最后一分钟的压力；而知觉型的人，
        # 认为过程更重要，需要大量信息才能做决定，容易摇摆，比较散漫，喜欢不同的经验，发现惊喜，常常有最后一分钟的爆发力。
        # 如果布置一个任务给两种类型的人，判断型的人会赶紧做计划，一步一步应该如何做？而知觉型的人，则可能先把任务放一边，
        # 到了快截止的时间才会重新拿起来。综上两者的差别是在于对事物的处理方式。（判断）
        if '事情' in i:
            # 从以上信息分析，作者推崇的是调整、分配、有计划目的性强的进行工作，以此推断为判断型
            # print(i)
            pass
    # print(f'{len(future)}:{len(now)}')#结果可以看出未来：显示比为3：13，所以我认为作者更偏向于直觉，脚踏实地的战略
    answer = """我认为作者人格为ENTJ，首先对于MBTI人格分析我从四个角度进行分析，内向-外向、实感-直觉、思维 — 情感、\n
              判断 — 知觉，首先对于内向-外向，我认为的关键点在于沟通（外向）如上信息可得作者在笔记中多数围绕着沟通\n
              和交流来发言，以上作者第一环节更加偏外向（直觉），其次对于实感-直觉，感是基于此物体往更加深层次去考虑\n
              ，而直觉则是直面这个物体。从而我认为其中差异在于看的有多远。结果可以看出未来：显示比为3（未来）：13（显示）\n
              ，所以我认为作者更偏向于直觉，脚踏实地的战略。然后对于思维 — 情感，问题一的检测中显示作者更偏向于理性（思维）\n
              最后对于判断 — 知觉，两者的差别是在于对事物的处理方式。从以上信息分析，作者推崇的是调整、分配、有计划目的性\n
              强的进行工作，以此推断为判断型。所以我认为作者是ENTJ人格"""
    return answer


def issue_four():
    """
    2012-4-2412:54 来自微博 weibo.com
    很香，感觉还没饱，但是我忍住了，立志不成为有啤酒肚的中年男
    抱歉，此微博己被作者删除。查看帮助：。网页链接
    这条内容表达作者什么思考
    :param data:
    :return:
    """
    answer = '如上问题可知，作者正处于一个创业期，机会和陷阱总是不断出现，赛道很长，如果一开始吃的过于饱的话，\n' \
             '可能无法到最后的起点，我想对于作者而言，可能认为永远保持奔跑的状态是最完美的。'
    return answer



data = get_pdf()
print('问题一：', issue_one(data))
print('问题二：',issue_two(data))
print('问题三：',issue_three(data))
print('问题四：',issue_four())
issue_four()
