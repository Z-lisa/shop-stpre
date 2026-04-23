<template>
  <transition name="fade">
    <div v-if="show" class="fixed inset-0 bg-black/50 z-100 flex items-end" @click.self="close">
      <div class="bg-white w-full rounded-t-2xl p-4 animate-slide-up z-100">
        <div class="flex items-center justify-between mb-4">
          <h3 class="text-lg font-bold text-gray-800">选择支付方式</h3>
          <button @click="close" class="text-gray-400">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="mb-4">
          <p class="text-sm text-gray-500 mb-1">支付金额</p>
          <p class="text-2xl text-primary font-bold">¥{{ totalPrice.toFixed(2) }}</p>
        </div>

        <div class="space-y-3 mb-4">
          <div 
            class="flex items-center justify-between p-4 border rounded-lg"
            :class="selectedMethod === 'wechat' ? 'border-primary bg-blue-50' : 'border-gray-200'"
            @click="selectedMethod = 'wechat'"
          >
            <div class="flex items-center gap-3">
              <span class="text-2xl">💚</span>
              <span class="font-medium text-gray-800">微信支付</span>
            </div>
            <div 
              class="w-5 h-5 rounded-full border-2 flex items-center justify-center"
              :class="selectedMethod === 'wechat' ? 'border-primary bg-primary' : 'border-gray-300'"
            >
              <svg v-if="selectedMethod === 'wechat'" class="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
            </div>
          </div>

          <div 
            class="flex items-center justify-between p-4 border rounded-lg"
            :class="selectedMethod === 'alipay' ? 'border-primary bg-blue-50' : 'border-gray-200'"
            @click="selectedMethod = 'alipay'"
          >
            <div class="flex items-center gap-3">
              <span class="text-2xl">💙</span>
              <span class="font-medium text-gray-800">支付宝</span>
            </div>
            <div 
              class="w-5 h-5 rounded-full border-2 flex items-center justify-center"
              :class="selectedMethod === 'alipay' ? 'border-primary bg-primary' : 'border-gray-300'"
            >
              <svg v-if="selectedMethod === 'alipay'" class="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
            </div>
          </div>
        </div>

        <button 
          class="w-full h-12 rounded-lg bg-primary text-white font-medium text-lg"
          :disabled="!selectedMethod"
          @click="confirmPay"
        >
          确认支付
        </button>
      </div>
    </div>
  </transition>

  <transition name="fade">
    <div v-if="showPayResult" class="fixed inset-0 bg-black/80 z-100 flex items-center justify-center">
      <div class="text-center">
        <div class="w-20 h-20 mx-auto mb-4 rounded-full flex items-center justify-center" :class="paySuccess ? 'bg-green-100' : 'bg-red-100'">
          <svg v-if="paySuccess" class="w-12 h-12 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
          </svg>
          <svg v-else class="w-12 h-12 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </div>
        <p class="text-white text-xl font-bold mb-2">{{ paySuccess ? '支付成功' : '支付失败' }}</p>
        <p v-if="paySuccess" class="text-gray-400 text-sm mb-4">{{ payMethodText }}支付 ¥{{ totalPrice.toFixed(2) }}</p>
        <button 
          v-if="paySuccess"
          class="px-8 h-10 rounded-lg bg-green-500 text-white font-medium"
          @click="goToOrderDetail"
        >
          查看订单
        </button>
        <button 
          v-else
          class="px-8 h-10 rounded-lg bg-red-500 text-white font-medium"
          @click="showPayResult = false"
        >
          重新支付
        </button>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  show: Boolean,
  totalPrice: {
    type: Number,
    default: 0
  },
  orderId: String
})

const emit = defineEmits(['close', 'success'])

const router = useRouter()
const selectedMethod = ref('wechat')
const showPayResult = ref(false)
const paySuccess = ref(false)

const payMethodText = computed(() => {
  return selectedMethod.value === 'wechat' ? '微信' : '支付宝'
})

const close = () => {
  emit('close')
}

const confirmPay = () => {
  showPayResult.value = true
  paySuccess.value = true
  
  setTimeout(() => {
    emit('success', {
      orderId: props.orderId,
      method: selectedMethod.value
    })
  }, 2000)
}

const goToOrderDetail = () => {
  showPayResult.value = false
  emit('close')
  router.push({ path: '/profile', query: { tab: 'orders' } })
}
</script>

<style scoped>
.animate-slide-up {
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from {
    transform: translateY(100%);
  }
  to {
    transform: translateY(0);
  }
}
</style>
