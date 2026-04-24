<template>
  <div class="min-h-screen bg-gray-50 pb-16">
    <div class="success-section flex flex-col items-center justify-center py-16 bg-white">
      <div class="success-icon w-20 h-20 rounded-full bg-green-100 flex items-center justify-center mb-6">
        <svg class="w-12 h-12 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
        </svg>
      </div>
      <h1 class="text-xl font-bold text-gray-800">订单提交成功</h1>
      <p class="text-sm text-gray-500 mt-2">感谢您的购买</p>
    </div>

    <div class="order-info bg-white mx-4 mt-2 rounded-lg p-4">
      <h2 class="text-sm font-bold text-gray-800 mb-3">订单信息</h2>
      <div class="space-y-2 text-sm">
        <div class="flex justify-between">
          <span class="text-gray-500">订单编号</span>
          <span class="text-gray-800">{{ order?.id || orderNumber }}</span>
        </div>
        <div class="flex justify-between">
          <span class="text-gray-500">订单金额</span>
          <span class="text-primary font-bold">¥{{ (order?.totalPrice || 0).toFixed(2) }}</span>
        </div>
        <div class="flex justify-between">
          <span class="text-gray-500">支付方式</span>
          <span class="text-gray-800">在线支付</span>
        </div>
        <div class="flex justify-between">
          <span class="text-gray-500">下单时间</span>
          <span class="text-gray-800">{{ order?.createTime || currentTime }}</span>
        </div>
      </div>
    </div>

    <div class="mt-6 px-4 space-y-3">
      <button 
        class="w-full h-11 rounded-lg bg-primary text-white font-medium"
        @click="goToOrders"
      >
        查看订单
      </button>
      <button 
        class="w-full h-11 rounded-lg border border-gray-300 text-gray-700 font-medium"
        @click="goToHome"
      >
        返回首页
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useOrderStore } from '../stores/order'

const router = useRouter()
const route = useRoute()
const orderStore = useOrderStore()

const orderNumber = ref('BK' + Date.now().toString().slice(-10))
const currentTime = ref(new Date().toLocaleString('zh-CN', { 
  year: 'numeric', 
  month: '2-digit', 
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit'
}))

const order = computed(() => {
  const orderId = route.query.orderId
  if (orderId) {
    return orderStore.getOrderById(orderId)
  }
  return null
})

const goToOrders = () => {
  router.replace({
    path: '/profile',
    query: { tab: 'orders' }
  })
}

const goToHome = () => {
  router.replace('/')
}
</script>
