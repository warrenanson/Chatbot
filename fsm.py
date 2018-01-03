
from transitions import Machine


class TocMachine(Machine):
	def __init__(self, **machine_configs):
		self.machine = Machine(
			model = self,
		**machine_configs
		)
	
	def is_going_to_user(self, update):
		text = update.message.text
		return text == 'Hi'
	
	def is_going_to_state1(self, update):
		text = update.message.text
		return text.lower() == '1'
		
	def is_going_to_bye(self, update):
		text = update.message.text
		return text.lower() == '2'
	
	def return_again(self, update):
		text = update.message.text
		return text.lower() == '3'	
		
	def _1_is_going_to_state2(self, update):
		text = update.message.text
		return text.lower() == '1'
		
	def _1_is_going_to_state3(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _2_is_going_to_state4(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _2_is_going_to_state5(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _3_is_going_to_state2(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _3_is_going_to_state5(self, update):
		text = update.message.text
		return text.lower() == '2'
	
	def _4_is_going_to_state6(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _4_is_going_to_state7(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _5_is_going_to_state4(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _5_is_going_to_state7(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _6_is_going_to_state8(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _6_is_going_to_state9(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _7_is_going_to_state6(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _7_is_going_to_state10(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _8_is_going_to_state11(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _8_is_going_to_state12(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _9_is_going_to_state8(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _9_is_going_to_state12(self, update):
		text = update.message.text
		return text.lower() == '2'
			
	def _10_is_going_to_state9(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _10_is_going_to_state13(self, update):
		text = update.message.text
		return text.lower() == '2'
			
	def _11_is_going_to_state14(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _11_is_going_to_state15(self, update):
		text = update.message.text
		return text.lower() == '2'
	
	def _12_is_going_to_state11(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _12_is_going_to_state15(self, update):
		text = update.message.text
		return text.lower() == '2'
			
	def _13_is_going_to_state12(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _13_is_going_to_state16(self, update):
		text = update.message.text
		return text.lower() == '2'
			
	def _14_is_going_to_state17(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _14_is_going_to_state18(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _15_is_going_to_state14(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _15_is_going_to_state18(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _16_is_going_to_state15(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _16_is_going_to_state19(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _17_is_going_to_state20(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _17_is_going_to_state21(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _18_is_going_to_state17(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _18_is_going_to_state21(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _19_is_going_to_state18(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _19_is_going_to_state22(self, update):
		text = update.message.text
		return text.lower() == '2'	
		
	def _20_is_going_to_stateA(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _20_is_going_to_stateB(self, update):
		text = update.message.text
		return text.lower() == '2'	
		
	def _21_is_going_to_state20(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _21_is_going_to_stateC(self, update):
		text = update.message.text
		return text.lower() == '2'
		
	def _22_is_going_to_state21(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def _22_is_going_to_stateD(self, update):
		text = update.message.text
		return text.lower() == '2'
	
	def useruser(self, update):
		text = update.message.text
		return text.lower() == '1'
	
	def byebye(self, update):
		text = update.message.text
		return text.lower() == '2'
	
	def on_enter_user(self, update):
		update.message.reply_text("請問是否開始心理測驗?\n(1)是\n(2)否\n(3)再問一次")
	
	def on_enter_bye(self, update):
		update.message.reply_text("不要拉倒")
	
	def on_enter_state1(self, update):
		update.message.reply_text("你會把自己比喻成哪種花香?\n(1)濃郁的花香\n(2)清淡的花香")
		
	
	def on_enter_state2(self, update):
		update.message.reply_text("你會選擇哪種香味的護唇膏?\n(1)水果味\n(2)薄荷味")

		
	def on_enter_state3(self, update):
		update.message.reply_text("你會把自己比喻為哪種花束?\n(1)紅色系(如紅、粉紅、橙)\n(2)非紅色系(如白、藍、紫)")
		
	
	def on_enter_state4(self, update):
		update.message.reply_text("你跟心上人首次約會用甚麼香水?\n(1)帶有甜味的花香\n(2)清爽的水果香味")

	
	def on_enter_state5(self, update):
		update.message.reply_text("你喜歡哪種味道?\n(1)盛夏乾燥的草味\n(2)雨後濕淋淋的草味")

	
	def on_enter_state6(self, update):
		update.message.reply_text("玫瑰和百合，你較喜歡哪種香味?\n(1)玫瑰\n(2)百合")
	
	def on_enter_state7(self, update):
		update.message.reply_text("你剛發現一瓶新款洗頭水，你十分喜歡它的味道，那瓶子的形狀是怎樣的?\n(1)圓形 \n(2)長身形 ")
	
	def on_enter_state8(self, update):
		update.message.reply_text("當你情緒低落時，哪種味道最能撫慰你的心靈？\n(1)花香 \n(2)森林的味道")
	
	def on_enter_state9(self, update):
		update.message.reply_text("你在收視超高的劇集中看見一個香包，它是什麼顏色？\n(1)紫色\n(2)紅色 ")
	
	def on_enter_state10(self, update):
		update.message.reply_text("市面剛推出了一種全新的香草味雪糕，你的看法是什麼？\n(1)相當引人注意\n(2)不太引人注意")
	
	def on_enter_state11(self, update):
		update.message.reply_text("下列哪種味道會勾起你懷念的感覺？\n(1)麵包香味\n(2)大自然的味道")
		
	def on_enter_state12(self, update):
		update.message.reply_text("如果月亮的光輝會發出味道，你嗅到後會聯想起下列哪組形容詞？\n(1)刺激 /燦爛奪目 /香味四溢\n(2)沉鬱 /弧獨 /踏實 /安靜")
	
	def on_enter_state13(self, update):
		update.message.reply_text("你較喜歡哪種香味？\n(1)香料 \n(2)茶香 ")
		
	def on_enter_state14(self, update):
		update.message.reply_text("如果月亮的光輝會發出味道，你嗅到後會聯想起下列哪組形容詞？\n(1)刺激 /燦爛奪目 /香味四溢\n(2)沉鬱 /弧獨 /踏實 /安靜")
		
	def on_enter_state15(self, update):
		update.message.reply_text(" 你覺得什麼香味較有助提神？\n(1)柑橘香\n(2)薄荷香")
		
	def on_enter_state16(self, update):
		update.message.reply_text(" 你喜歡異性身上有哪種香味？\n(1)香水味\n(2)自然肥皂")
		
	def on_enter_state17(self, update):
		update.message.reply_text("  想起遊樂場，你會想起哪種味道？\n(1)牛奶及葡萄\n(2)甜甜的糖果")
		
	def on_enter_state18(self, update):
		update.message.reply_text(" 如果要在房間燃點香薰，你喜歡哪一種形狀的香薰？\n(1)三角錐形\n(2)棒狀")
		
	def on_enter_state19(self, update):
		update.message.reply_text(" 你對於香水的看法是？\n(1)非常喜歡\n(2)不算十分喜歡 ")
		
	def on_enter_state20(self, update):
		update.message.reply_text(" 對於嬰兒使用的肥皂系列香味有什麼看法？\n(1)喜歡\n(2)不是特別喜歡 ")
		
	def on_enter_state21(self, update):
		update.message.reply_text(" 你知道自己的味道嗎？\n(1)不知道\n(2)知道 ")
		
	def on_enter_state22(self, update):
		update.message.reply_text(" 喜歡皮革的味道嗎？\n(1)喜歡\n(2)討厭 ")
	
	def on_enter_stateA(self, update):
		update.message.reply_text("A. 你是屬於水果香形象\n\n\n你充滿自由愉悅的氣息，總是沉溺左遊樂場當中，像個天真無邪的孩子。\n\n有你在的地方，整個氣氛都會興奮起來，所以你是聚會中不可或缺的人物。\n\n雖說你個性開朗，受到大部份人的喜愛，但別人一般認為難以跟你成為親密好友，即是說，你給人的印象只是個搞笑能手\n\n有些人覺得你愛玩弄別人，依賴性又強，所以不太願意親近你。\n\n不過，真正的你其實十分成熟穩重，正因透徹了解你的人不多，所以知己朋友也相當少。\n")
		self.gofinal(update)
	def on_enter_stateB(self, update):
		update.message.reply_text("B. 你是屬於東方花香形象\n\n\n你擁有強烈的自我意識及自己的世界，不會被他人玩弄於股掌之間，會利用自己的力量積極地達成願望，給人有熱情的印象。\n\n你不會跟朋友糾纏不清，再加上給人單獨行動的印象，圍繞在你週遭的人都會覺得你是一個「帶有神秘色彩的人物」。\n\n「神秘感」有時是相當有魅力的意思，但是人們對於你嚴密的防備以及自命清高的態度，感覺無法輕鬆地與你對談而覺得你難以應付，甚而變成非必要不跟你接觸, 對你敬而遠之的傾向。\n\n真正的你其實是相當溫柔的，但是除非是與你相當親近的，否則是無法注意到你的優點。\n")
		self.gofinal(update)
	def on_enter_stateC(self, update):
		update.message.reply_text("C. 你是屬於草香形象\n\n\n你擁有非常堅強的意志，不依賴他人，給人獨來獨往的印象。\n\n你擁有旺盛的好奇心與豐富的感受性，是個過著知性生活的現代人。\n\n驟看下你是個自命清高，不好相處的人，但是一旦跟你交談後，就知道你很好相處，等到交情加深之後，就更知道你其實擁有很爽快的個性。\n\n你所擁有的中性化魅力，讓你不論在男性團體或女性團體都大受歡迎，不過你不喜歡讓人看到你脆弱的一面。\n\n你外表上看來也許很冷靜，但實際上卻是熱情如火能夠知道你真正本性的人，才能夠跟你天長地久地交往下去。\n")
		self.gofinal(update)
	def on_enter_stateD(self, update):
		update.message.reply_text("D. 你是屬於花香形象\n\n\n你總是給人樂觀、積極和勇於面對困難的感覺，而且溫柔優雅，很懂得為他人設想，給人非常擅長維繫人際關係的印象。\n\n這樣的你讓人感到既堅強又脆弱，尤其是你那關懷體貼的包容力，更讓人覺得你相當有魅力，很值得信賴。\n\n你長期給人認為你是個「拜託做事絕不會拒絕」的人，所以特別容易讓依賴心強、只顧自己利益的人利用。\n\n這些人因為看中你細心隨和的一面，所以會故意親近你，然後借故佔你便宜。\n")
		self.gofinal(update)
	def on_enter_finish(self, update):
		update.message.reply_text("請問是否重新測驗?\n(1)是\n(2)否")
		
		
	
	
	