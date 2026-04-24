<template>
  <div class="min-h-screen bg-gray-50 pb-16">
    <template v-if="activeTab === 'home'">
      <div class="bg-primary px-4 py-6">
        <div class="flex items-center gap-4">
          <div class="w-16 h-16 rounded-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center shadow-lg">
            <span class="text-white text-2xl font-bold">{{ userStore.userInfo?.name?.charAt(0) || '游' }}</span>
          </div>
          <div class="flex-1">
            <h1 class="text-white text-lg font-bold">{{ userStore.userInfo?.name || '游客' }}</h1>
            <p class="text-white/70 text-sm mt-1">
              {{ userStore.isGuest ? '登录后享受更多服务' : '欢迎来到购物商城' }}
            </p>
          </div>
          <button 
            v-if="userStore.isGuest"
            class="px-4 py-2 bg-white/20 rounded-full text-white text-sm"
            @click="router.push('/login')"
          >
            登录
          </button>
          <button 
            v-else
            class="px-4 py-2 bg-white/20 rounded-full text-white text-sm"
            @click="handleLogout"
          >
            退出
          </button>
        </div>
      </div>

      <div class="px-4 -mt-4">
        <div class="bg-white rounded-lg shadow-sm p-4 flex justify-around">
          <div class="flex flex-col items-center" @click="activeTab = 'favorites'">
            <span class="text-xl text-red-500">♥</span>
            <span class="text-xs text-gray-600 mt-1">收藏</span>
            <span class="text-xs text-gray-400">{{ favoritesStore.favoritesCount }}</span>
          </div>
          <div class="flex flex-col items-center" @click="activeTab = 'orders'">
            <span class="text-xl text-primary">📋</span>
            <span class="text-xs text-gray-600 mt-1">订单</span>
            <span class="text-xs text-gray-400">{{ orderStore.orders.length }}</span>
          </div>
          <div class="flex flex-col items-center" @click="router.push('/coupons')">
            <span class="text-xl text-orange-500">🎫</span>
            <span class="text-xs text-gray-600 mt-1">优惠券</span>
            <span class="text-xs text-gray-400">{{ couponStore.availableUserCoupons.length }}</span>
          </div>
        </div>
      </div>

      <div class="mt-4 bg-white">
        <div class="menu-item px-4 py-4 flex items-center justify-between border-b" @click="activeTab = 'orders'">
          <div class="flex items-center gap-3">
            <span class="text-lg">📦</span>
            <span class="text-sm text-gray-700">我的订单</span>
          </div>
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </div>
        <div class="menu-item px-4 py-4 flex items-center justify-between border-b" @click="activeTab = 'favorites'">
          <div class="flex items-center gap-3">
            <span class="text-lg">❤️</span>
            <span class="text-sm text-gray-700">我的收藏</span>
          </div>
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </div>
        <div class="menu-item px-4 py-4 flex items-center justify-between border-b" @click="router.push('/address')">
          <div class="flex items-center gap-3">
            <span class="text-lg">📍</span>
            <span class="text-sm text-gray-700">地址管理</span>
          </div>
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </div>
        <div class="menu-item px-4 py-4 flex items-center justify-between border-b" @click="router.push('/coupons')">
          <div class="flex items-center gap-3">
            <span class="text-lg">🎫</span>
            <span class="text-sm text-gray-700">优惠券</span>
          </div>
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </div>
        <div class="menu-item px-4 py-4 flex items-center justify-between border-b" @click="router.push('/customer-service')">
          <div class="flex items-center gap-3">
            <span class="text-lg">💬</span>
            <span class="text-sm text-gray-700">客服中心</span>
          </div>
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </div>
        <div class="menu-item px-4 py-4 flex items-center justify-between" @click="router.push('/about-us')">
          <div class="flex items-center gap-3">
            <span class="text-lg">ℹ️</span>
            <span class="text-sm text-gray-700">关于我们</span>
          </div>
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </div>
        <div class="menu-item px-4 py-4 flex items-center justify-between" @click="router.push('/clear-data')">
          <div class="flex items-center gap-3">
            <span class="text-lg">🗑️</span>
            <span class="text-sm text-gray-700">清空数据</span>
          </div>
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </div>
      </div>
    </template>

    <template v-else-if="activeTab === 'favorites'">
      <div class="bg-primary px-4 py-3">
        <div class="flex items-center gap-3">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" @click="activeTab = 'home'">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
          <h1 class="text-white text-lg font-bold">我的收藏</h1>
        </div>
      </div>

      <div v-if="favoritesStore.favorites.length > 0" class="favorites-list px-4 py-4">
        <div 
          v-for="book in favoritesStore.favorites" 
          :key="book.id"
          class="favorite-item bg-white rounded-lg p-3 mb-3 flex gap-3 shadow-sm"
          @click="goToDetail(book.id)"
        >
          <img :src="book.cover" :alt="book.name" class="w-20 h-24 object-cover rounded flex-shrink-0" />
          <div class="flex-1 min-w-0">
            <h3 class="text-sm font-medium text-gray-800 truncate">{{ book.name }}</h3>
            <p class="text-xs text-gray-500 mt-1 truncate">{{ book.author }}</p>
            <div class="flex items-center justify-between mt-2">
              <span class="text-sm text-primary font-bold">¥{{ book.price }}</span>
              <button 
                class="text-xs text-gray-400"
                @click.stop="removeFavorite(book.id)"
              >
                取消收藏
              </button>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="empty-favorites flex flex-col items-center justify-center py-20">
        <svg class="w-20 h-20 text-gray-300" fill="currentColor" viewBox="0 0 24 24">
          <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
        </svg>
        <p class="text-gray-400 mt-4">还没有收藏</p>
        <button class="mt-4 px-6 py-2 bg-primary text-white rounded-lg text-sm" @click="goShopping">
          去逛逛
        </button>
      </div>
    </template>

    <template v-else-if="activeTab === 'orders'">
      <div class="bg-primary px-4 py-3">
        <div class="flex items-center gap-3">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" @click="activeTab = 'home'">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
          <h1 class="text-white text-lg font-bold">我的订单</h1>
        </div>
      </div>

      <div class="order-tabs bg-white flex overflow-x-auto border-b">
        <div 
          v-for="tab in orderTabs" 
          :key="tab.value"
          class="flex-shrink-0 px-4 py-3 text-sm font-medium transition-colors"
          :class="orderStatus === tab.value ? 'text-primary border-b-2 border-primary' : 'text-gray-500'"
          @click="orderStatus = tab.value"
        >
          {{ tab.label }}
        </div>
      </div>

      <div v-if="displayOrders.length > 0" class="orders-list px-4 py-4 space-y-4">
        <div 
          v-for="order in displayOrders" 
          :key="order.id"
          class="order-card bg-white rounded-lg overflow-hidden shadow-sm"
          @click="goToOrderDetail(order.id)"
        >
          <div class="px-4 py-3 bg-gray-50 flex items-center justify-between">
            <div>
              <span class="text-xs text-gray-500">订单号: {{ order.id }}</span>
              <p class="text-xs text-gray-400 mt-1">{{ order.createTime }}</p>
            </div>
            <div class="flex items-center gap-2">
              <span 
                class="px-2 py-1 rounded text-xs font-medium"
                :class="getStatusClass(order.status)"
              >
                {{ getStatusText(order.status) }}
              </span>
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </div>
          </div>

          <div class="p-4">
            <div 
              v-for="item in order.items" 
              :key="item.id"
              class="flex items-center gap-3 mb-3 last:mb-0 cursor-pointer"
              @click="goToDetail(item.id)"
            >
              <img :src="item.cover" :alt="item.name" class="w-16 h-20 object-cover rounded" />
              <div class="flex-1">
                <h3 class="text-sm font-medium text-gray-800 truncate">{{ item.name }}</h3>
                <p class="text-xs text-gray-500 mt-1">{{ item.author }}</p>
                <div class="flex items-center justify-between mt-1">
                  <span class="text-sm text-primary font-bold">¥{{ item.price }}</span>
                  <span class="text-xs text-gray-400">x{{ item.quantity }}</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-4 py-3 border-t flex items-center justify-between">
            <span class="text-sm text-gray-500">合计: <span class="text-primary font-bold">¥{{ order.totalPrice.toFixed(2) }}</span></span>
            <div class="flex gap-2">
              <button 
                v-if="order.status === 'pending'"
                class="px-3 py-1.5 text-xs border border-gray-300 rounded-lg text-gray-600"
                @click="openPayModal(order)"
              >
                去支付
              </button>
              <button 
                v-if="order.status === 'paid'"
                class="px-3 py-1.5 text-xs border border-gray-300 rounded-lg text-gray-600"
                @click="simulateShip(order.id)"
              >
                模拟发货
              </button>
              <button 
                v-if="order.status === 'shipped'"
                class="px-3 py-1.5 text-xs border border-primary rounded-lg text-primary"
                @click="orderStore.completeOrder(order.id)"
              >
                确认收货
              </button>
              <button 
                class="px-3 py-1.5 text-xs border border-gray-300 rounded-lg text-gray-600"
                @click="goToDetail(order.items[0]?.id)"
              >
                再次购买
              </button>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="empty-orders flex flex-col items-center justify-center py-20">
        <svg class="w-20 h-20 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
        </svg>
        <p class="text-gray-400 mt-4">暂无订单</p>
        <button class="mt-4 px-6 py-2 bg-primary text-white rounded-lg text-sm" @click="goShopping">
          去逛逛
        </button>
      </div>

      <PayModal 
        v-if="payingOrder"
        :show="showPayModal" 
        :total-price="payingOrder.totalPrice"
        :order-id="payingOrder.id"
        @close="showPayModal = false"
        @success="handlePaySuccess"
      />
    </template>
  </div>

</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useFavoritesStore } from '../stores/favorites'
import { useOrderStore } from '../stores/order'
import { useUserStore } from '../stores/user'
import { useCouponStore } from '../stores/coupon'
import PayModal from '../components/PayModal.vue'

const router = useRouter()
const route = useRoute()
const favoritesStore = useFavoritesStore()
const orderStore = useOrderStore()
const userStore = useUserStore()
const couponStore = useCouponStore()

const activeTab = ref('home')
const orderStatus = ref('all')
const showPayModal = ref(false)
const payingOrder = ref(null)

const orderTabs = [
  { label: '全部', value: 'all' },
  { label: '待付款', value: 'pending' },
  { label: '待发货', value: 'paid' },
  { label: '待收货', value: 'shipped' },
  { label: '已完成', value: 'completed' }
]

const displayOrders = computed(() => {
  return orderStore.getOrdersByStatus(orderStatus.value)
})

const removeFavorite = (bookId) => {
  favoritesStore.removeFavorite(bookId)
}

const goToDetail = (bookId) => {
  if (bookId) {
    router.push(`/book/${bookId}`)
  }
}

const goToOrderDetail = (orderId) => {
  if (orderId) {
    router.push(`/order/${orderId}`)
  }
}

const goShopping = () => {
  activeTab.value = 'home'
  router.push('/')
}

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

const openPayModal = (order) => {
  payingOrder.value = order
  showPayModal.value = true
}

const handlePaySuccess = (data) => {
  orderStore.payOrder(data.orderId, data.method)
  showPayModal.value = false
  payingOrder.value = null
}

const simulateShip = (orderId) => {
  orderStore.shipOrder(orderId)
}

const handleLogout = () => {
  userStore.logout()
  router.push('/login')
}

onMounted(() => {
  if (route.query.tab === 'orders') {
    activeTab.value = 'orders'
  } else if (route.query.tab === 'favorites') {
    activeTab.value = 'favorites'
  }
})

watch(() => route.query.tab, (newTab) => {
  if (newTab === 'orders') {
    activeTab.value = 'orders'
  } else if (newTab === 'favorites') {
    activeTab.value = 'favorites'
  }
})
</script>
