<template>
  <div class="min-h-screen bg-gray-50 pb-16">
    <div class="bg-primary px-4 py-3">
      <div class="flex items-center gap-3">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" @click="goBack">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        <h1 class="text-white text-lg font-bold">订单详情</h1>
      </div>
    </div>

    <div v-if="order" class="space-y-3 px-4 py-4">
      <!-- 订单状态 -->
      <div class="bg-white rounded-lg p-4">
        <div class="flex items-center justify-between">
          <div>
            <span class="text-sm text-gray-500">订单号: {{ order.id }}</span>
            <p class="text-xs text-gray-400 mt-1">{{ order.createTime }}</p>
          </div>
          <span 
            class="px-3 py-1 rounded text-sm font-medium"
            :class="getStatusClass(order.status)"
          >
            {{ getStatusText(order.status) }}
          </span>
        </div>
        
        <!-- VIP标识 -->
        <div v-if="order.isVIPOrder" class="mt-3 flex items-center gap-2 bg-gradient-to-r from-purple-50 to-pink-50 p-2 rounded">
          <span class="text-purple-500">💎</span>
          <span class="text-xs text-purple-600">VIP会员订单 (85折优惠)</span>
        </div>
      </div>

      <!-- 收货地址 -->
      <div class="bg-white rounded-lg p-4">
        <h3 class="text-sm font-bold text-gray-800 mb-3">收货信息</h3>
        <div class="flex items-center gap-3">
          <span class="text-xl">📍</span>
          <div class="flex-1">
            <p class="text-sm font-medium text-gray-800">{{ order.address?.name }} {{ order.address?.phone }}</p>
            <p class="text-xs text-gray-500 mt-1">{{ order.address?.province }}{{ order.address?.city }}{{ order.address?.district }} {{ order.address?.detail }}</p>
          </div>
        </div>
      </div>

      <!-- 商品清单 -->
      <div class="bg-white rounded-lg p-4">
        <h3 class="text-sm font-bold text-gray-800 mb-3">商品清单</h3>
        <div class="space-y-3">
          <div 
            v-for="item in order.items" 
            :key="item.id"
            class="flex items-center gap-3"
            @click="goToBookDetail(item.id)"
          >
            <img :src="item.cover" :alt="item.name" class="w-16 h-20 object-cover rounded" />
            <div class="flex-1">
              <h4 class="text-sm font-medium text-gray-800 truncate">{{ item.name }}</h4>
              <p class="text-xs text-gray-500 mt-1">{{ item.author }}</p>
              <div class="flex items-center justify-between mt-2">
                <span class="text-sm text-primary font-bold">¥{{ item.price }}</span>
                <span class="text-xs text-gray-400">x{{ item.quantity }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 订单备注 -->
      <div v-if="order.note" class="bg-white rounded-lg p-4">
        <h3 class="text-sm font-bold text-gray-800 mb-3">订单备注</h3>
        <div class="bg-gray-50 p-3 rounded">
          <p class="text-sm text-gray-700">{{ order.note }}</p>
        </div>
      </div>

      <!-- 价格明细 -->
      <div class="bg-white rounded-lg p-4">
        <h3 class="text-sm font-bold text-gray-800 mb-3">价格明细</h3>
        <div class="space-y-2">
          <div class="flex justify-between text-sm">
            <span class="text-gray-500">商品金额</span>
            <span class="text-gray-800">¥{{ order.originalPrice?.toFixed(2) || order.totalPrice.toFixed(2) }}</span>
          </div>
          
          <div v-if="order.isVIPOrder" class="flex justify-between text-sm">
            <span class="text-gray-500">VIP会员折扣 (85折)</span>
            <span class="text-price-orange">-¥{{ ((order.originalPrice || order.totalPrice) * 0.15).toFixed(2) }}</span>
          </div>
          
          <div class="flex justify-between text-sm">
            <span class="text-gray-500">运费</span>
            <span class="text-gray-800">¥0.00</span>
          </div>
          
          <div class="flex justify-between text-base pt-2 border-t">
            <span class="font-medium text-gray-800">实付金额</span>
            <span class="text-primary font-bold">¥{{ order.totalPrice.toFixed(2) }}</span>
          </div>
        </div>
      </div>

      <!-- 时间线 -->
      <div class="bg-white rounded-lg p-4">
        <h3 class="text-sm font-bold text-gray-800 mb-3">订单进度</h3>
        <div class="space-y-4">
          <div class="flex items-start gap-3">
            <div class="w-2 h-2 bg-primary rounded-full mt-1.5"></div>
            <div>
              <p class="text-sm text-gray-800">订单创建</p>
              <p class="text-xs text-gray-400 mt-1">{{ order.createTime }}</p>
            </div>
          </div>
          
          <div v-if="order.payTime" class="flex items-start gap-3">
            <div class="w-2 h-2 bg-primary rounded-full mt-1.5"></div>
            <div>
              <p class="text-sm text-gray-800">支付成功</p>
              <p class="text-xs text-gray-400 mt-1">{{ order.payTime }}</p>
            </div>
          </div>
          
          <div v-if="order.shipTime" class="flex items-start gap-3">
            <div class="w-2 h-2 bg-primary rounded-full mt-1.5"></div>
            <div>
              <p class="text-sm text-gray-800">商品发货</p>
              <p class="text-xs text-gray-400 mt-1">{{ order.shipTime }}</p>
            </div>
          </div>
          
          <div v-if="order.completeTime" class="flex items-start gap-3">
            <div class="w-2 h-2 bg-primary rounded-full mt-1.5"></div>
            <div>
              <p class="text-sm text-gray-800">订单完成</p>
              <p class="text-xs text-gray-400 mt-1">{{ order.completeTime }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 操作按钮 -->
      <div class="bg-white rounded-lg p-4">
        <div class="flex gap-3">
          <button 
            v-if="order.status === 'pending'"
            class="flex-1 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium"
            @click="openPayModal"
          >
            去支付
          </button>
          <button 
            v-if="order.status === 'paid'"
            class="flex-1 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium"
            @click="simulateShip"
          >
            模拟发货
          </button>
          <button 
            v-if="order.status === 'shipped'"
            class="flex-1 px-4 py-2 bg-primary text-white rounded-lg text-sm font-medium"
            @click="completeOrder"
          >
            确认收货
          </button>
          <button 
            class="flex-1 px-4 py-2 border border-gray-300 text-gray-600 rounded-lg text-sm"
            @click="goToBookDetail(order.items[0]?.id)"
          >
            再次购买
          </button>
        </div>
      </div>
    </div>

    <div v-else class="flex flex-col items-center justify-center py-20">
      <svg class="w-20 h-20 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
      </svg>
      <p class="text-gray-400 mt-4">订单不存在</p>
      <button class="mt-4 px-6 py-2 bg-primary text-white rounded-lg text-sm" @click="goBack">
        返回
      </button>
    </div>

    <PayModal 
      v-if="order"
      :show="showPayModal" 
      :total-price="order.totalPrice"
      :order-id="order.id"
      @close="showPayModal = false"
      @success="handlePaySuccess"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useOrderStore } from '../stores/order'
import PayModal from '../components/PayModal.vue'

const router = useRouter()
const route = useRoute()
const orderStore = useOrderStore()

const order = ref(null)
const showPayModal = ref(false)

const getStatusClass = (status) => {
  const classes = {
    pending: 'bg-orange-100 text-orange-600',
    paid: 'bg-blue-100 text-blue-600',
    shipped: 'bg-purple-100 text-purple-600',
    completed: 'bg-green-100 text-green-600'
  }
  return classes[status] || 'bg-gray-100 text-gray-600'
}

const getStatusText = (status) => {
  const texts = {
    pending: '待付款',
    paid: '待发货',
    shipped: '待收货',
    completed: '已完成'
  }
  return texts[status] || status
}

const goBack = () => {
  router.back()
}

const goToBookDetail = (bookId) => {
  if (bookId) {
    router.push(`/book/${bookId}`)
  }
}

const openPayModal = () => {
  showPayModal.value = true
}

const handlePaySuccess = (data) => {
  orderStore.payOrder(data.orderId, data.method)
  // 刷新订单数据
  order.value = orderStore.getOrderById(data.orderId)
}

const simulateShip = () => {
  orderStore.shipOrder(order.value.id)
  // 刷新订单数据
  order.value = orderStore.getOrderById(order.value.id)
}

const completeOrder = () => {
  orderStore.completeOrder(order.value.id)
  // 刷新订单数据
  order.value = orderStore.getOrderById(order.value.id)
}

onMounted(() => {
  const orderId = route.params.id
  if (orderId) {
    order.value = orderStore.getOrderById(orderId)
  }
})
</script>

<style scoped>
.text-price-orange {
  color: #ff6b35;
}
</style>