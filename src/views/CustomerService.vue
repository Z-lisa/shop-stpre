<template>
  <div class="min-h-screen bg-gray-50 flex flex-col pb-16">
    <div class="bg-primary px-4 py-3">
      <div class="flex items-center gap-3">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" @click="goBack">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        <h1 class="text-white text-lg font-bold">客服中心</h1>
      </div>
    </div>

    <div class="flex-1 overflow-y-auto p-4 space-y-4" ref="chatContainer">
      <div class="flex items-start gap-3">
        <div class="w-10 h-10 rounded-full bg-primary flex items-center justify-center flex-shrink-0">
          <span class="text-white text-lg">🤖</span>
        </div>
        <div class="bg-white rounded-lg p-3 max-w-[80%] shadow-sm">
          <p class="text-sm text-gray-800">您好！我是购物商城智能客服，请问有什么可以帮助您的？</p>
          <p class="text-xs text-gray-400 mt-2">{{ currentTime }}</p>
        </div>
      </div>

      <div v-for="(msg, index) in messages" :key="index" class="flex items-start gap-3" :class="msg.type === 'user' ? 'flex-row-reverse' : ''">
        <div v-if="msg.type === 'bot'" class="w-10 h-10 rounded-full bg-primary flex items-center justify-center flex-shrink-0">
          <span class="text-white text-lg">🤖</span>
        </div>
        <div v-else class="w-10 h-10 rounded-full bg-gray-300 flex items-center justify-center flex-shrink-0">
          <span class="text-white text-lg">👤</span>
        </div>
        <div class="rounded-lg p-3 max-w-[80%] shadow-sm" :class="msg.type === 'user' ? 'bg-primary text-white' : 'bg-white'">
          <p class="text-sm" :class="msg.type === 'user' ? 'text-white' : 'text-gray-800'">{{ msg.content }}</p>
          <p class="text-xs mt-2" :class="msg.type === 'user' ? 'text-white/70' : 'text-gray-400'">{{ msg.time }}</p>
        </div>
      </div>

      <div v-if="isTyping" class="flex items-start gap-3">
        <div class="w-10 h-10 rounded-full bg-primary flex items-center justify-center flex-shrink-0">
          <span class="text-white text-lg">🤖</span>
        </div>
        <div class="bg-white rounded-lg p-3 shadow-sm">
          <div class="flex gap-1">
            <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></span>
            <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.1s"></span>
            <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.2s"></span>
          </div>
        </div>
      </div>
    </div>

    <div class="bg-white border-t p-4 safe-area-bottom">
      <div class="flex gap-2 mb-3 overflow-x-auto pb-2">
        <button 
          v-for="(question, index) in quickQuestions" 
          :key="index"
          class="flex-shrink-0 px-3 py-1.5 bg-gray-100 rounded-full text-xs text-gray-600"
          @click="sendQuickQuestion(question)"
        >
          {{ question }}
        </button>
      </div>
      <div class="flex gap-2">
        <input 
          v-model="inputMessage"
          type="text" 
          placeholder="请输入您的问题..."
          class="flex-1 h-10 px-4 border border-gray-200 rounded-full text-sm"
          @keyup.enter="sendMessage"
        />
        <button 
          class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center"
          :disabled="!inputMessage.trim()"
          @click="sendMessage"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, nextTick } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const chatContainer = ref(null)
const inputMessage = ref('')
const messages = ref([])
const isTyping = ref(false)

const currentTime = computed(() => {
  return new Date().toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' })
})

const quickQuestions = [
  '如何下单？',
  '配送时间',
  '退换货政策',
  '优惠券使用',
  '支付方式'
]

const knowledgeBase = {
  '下单': '下单流程：1. 选择购物加入购物车 2. 进入购物车结算 3. 选择收货地址 4. 确认支付',
  '配送': '配送时间：一般1-3个工作日送达，偏远地区3-5个工作日。满99元免运费。',
  '退换': '退换货政策：支持7天无理由退货，购物需保持完好。质量问题免费退换。',
  '优惠': '优惠券使用：在结算页面选择可用优惠券，系统会自动计算优惠金额。',
  '支付': '支付方式：支持微信支付、支付宝支付，以及银行卡支付。',
  '默认': '抱歉，我可能没有完全理解您的问题。您可以尝试询问：如何下单、配送时间、退换货政策、优惠券使用、支付方式等。'
}

const goBack = () => {
  router.back()
}

const scrollToBottom = () => {
  nextTick(() => {
    if (chatContainer.value) {
      chatContainer.value.scrollTop = chatContainer.value.scrollHeight
    }
  })
}

const getBotReply = (userMessage) => {
  const message = userMessage.toLowerCase()
  
  for (const [key, reply] of Object.entries(knowledgeBase)) {
    if (message.includes(key)) {
      return reply
    }
  }
  
  // 智能匹配
  if (message.includes('价格') || message.includes('多少钱')) {
    return '购物价格以页面显示为准，新用户注册可领取优惠券享受折扣。'
  }
  if (message.includes('库存') || message.includes('有货')) {
    return '商品页面会显示实时库存，如显示"有货"即可正常下单购买。'
  }
  if (message.includes('会员') || message.includes('积分')) {
    return '注册会员可享受积分累积，积分可用于抵扣订单金额。'
  }
  if (message.includes('发票')) {
    return '下单时可选择开具电子发票，发票会在订单完成后发送至您的邮箱。'
  }
  if (message.includes('客服') || message.includes('人工')) {
    return '智能客服24小时在线，如需人工客服请拨打：400-123-4567（工作日9:00-18:00）'
  }
  
  return knowledgeBase['默认']
}

const sendMessage = () => {
  if (!inputMessage.value.trim()) return
  
  const userMsg = inputMessage.value.trim()
  messages.value.push({
    type: 'user',
    content: userMsg,
    time: currentTime.value
  })
  
  inputMessage.value = ''
  scrollToBottom()
  
  // 模拟机器人思考
  isTyping.value = true
  scrollToBottom()
  
  setTimeout(() => {
    isTyping.value = false
    const reply = getBotReply(userMsg)
    messages.value.push({
      type: 'bot',
      content: reply,
      time: currentTime.value
    })
    scrollToBottom()
  }, 1000 + Math.random() * 1000)
}

const sendQuickQuestion = (question) => {
  inputMessage.value = question
  sendMessage()
}
</script>

<style scoped>
.safe-area-bottom {
  padding-bottom: env(safe-area-inset-bottom);
}

.animate-bounce {
  animation: bounce 1s infinite;
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-4px);
  }
}
</style>
