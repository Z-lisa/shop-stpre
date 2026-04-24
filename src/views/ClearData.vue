<template>
  <div class="min-h-screen bg-gray-50 pb-16">
    <div class="bg-primary px-4 py-3">
      <div class="flex items-center gap-3">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" @click="goBack">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        <h1 class="text-white text-lg font-bold">清空数据</h1>
      </div>
    </div>

    <div class="p-4 space-y-4">
      <!-- 警告提示 -->
      <div class="bg-orange-50 border border-orange-200 rounded-lg p-4">
        <div class="flex items-center gap-2 mb-2">
          <span class="text-orange-500 text-lg">⚠️</span>
          <span class="text-sm font-medium text-orange-800">重要提示</span>
        </div>
        <p class="text-xs text-orange-700">
          清空数据操作不可恢复！这将删除所有本地存储的用户数据，包括订单、购物车、收藏等。
        </p>
      </div>

      <!-- 数据统计 -->
      <div class="bg-white rounded-lg shadow-sm p-4">
        <h3 class="text-sm font-bold text-gray-800 mb-3">当前数据统计</h3>
        <div class="grid grid-cols-2 gap-4 text-sm">
          <div class="flex flex-col items-center p-3 bg-gray-50 rounded">
            <span class="text-gray-500">购物车</span>
            <span class="text-primary font-bold mt-1">{{ cartCount }} 件</span>
          </div>
          <div class="flex flex-col items-center p-3 bg-gray-50 rounded">
            <span class="text-gray-500">订单</span>
            <span class="text-primary font-bold mt-1">{{ orderCount }} 个</span>
          </div>
          <div class="flex flex-col items-center p-3 bg-gray-50 rounded">
            <span class="text-gray-500">收藏</span>
            <span class="text-primary font-bold mt-1">{{ favoriteCount }} 件</span>
          </div>
          <div class="flex flex-col items-center p-3 bg-gray-50 rounded">
            <span class="text-gray-500">地址</span>
            <span class="text-primary font-bold mt-1">{{ addressCount }} 个</span>
          </div>
        </div>
      </div>

      <!-- 清空选项 -->
      <div class="bg-white rounded-lg shadow-sm p-4">
        <h3 class="text-sm font-bold text-gray-800 mb-3">清空选项</h3>
        <div class="space-y-3">
          <label class="flex items-center gap-3 p-3 border border-gray-200 rounded-lg cursor-pointer">
            <input type="checkbox" v-model="clearCart" class="w-4 h-4 text-primary rounded">
            <div class="flex-1">
              <span class="text-sm font-medium text-gray-800">清空购物车</span>
              <p class="text-xs text-gray-500 mt-1">删除购物车中的所有商品</p>
            </div>
            <span class="text-xs text-gray-400">{{ cartCount }} 件</span>
          </label>

          <label class="flex items-center gap-3 p-3 border border-gray-200 rounded-lg cursor-pointer">
            <input type="checkbox" v-model="clearOrders" class="w-4 h-4 text-primary rounded">
            <div class="flex-1">
              <span class="text-sm font-medium text-gray-800">清空订单</span>
              <p class="text-xs text-gray-500 mt-1">删除所有订单记录</p>
            </div>
            <span class="text-xs text-gray-400">{{ orderCount }} 个</span>
          </label>

          <label class="flex items-center gap-3 p-3 border border-gray-200 rounded-lg cursor-pointer">
            <input type="checkbox" v-model="clearFavorites" class="w-4 h-4 text-primary rounded">
            <div class="flex-1">
              <span class="text-sm font-medium text-gray-800">清空收藏</span>
              <p class="text-xs text-gray-500 mt-1">删除所有收藏商品</p>
            </div>
            <span class="text-xs text-gray-400">{{ favoriteCount }} 件</span>
          </label>

          <label class="flex items-center gap-3 p-3 border border-gray-200 rounded-lg cursor-pointer">
            <input type="checkbox" v-model="clearAddresses" class="w-4 h-4 text-primary rounded">
            <div class="flex-1">
              <span class="text-sm font-medium text-gray-800">清空地址</span>
              <p class="text-xs text-gray-500 mt-1">删除所有收货地址</p>
            </div>
            <span class="text-xs text-gray-400">{{ addressCount }} 个</span>
          </label>

          <label class="flex items-center gap-3 p-3 border border-gray-200 rounded-lg cursor-pointer">
            <input type="checkbox" v-model="clearCoupons" class="w-4 h-4 text-primary rounded">
            <div class="flex-1">
              <span class="text-sm font-medium text-gray-800">清空优惠券</span>
              <p class="text-xs text-gray-500 mt-1">删除所有优惠券记录</p>
            </div>
            <span class="text-xs text-gray-400">{{ couponCount }} 张</span>
          </label>

          <label class="flex items-center gap-3 p-3 border border-gray-200 rounded-lg cursor-pointer">
            <input type="checkbox" v-model="clearAll" class="w-4 h-4 text-primary rounded" @change="handleSelectAll">
            <div class="flex-1">
              <span class="text-sm font-medium text-gray-800">全选</span>
              <p class="text-xs text-gray-500 mt-1">清空所有数据</p>
            </div>
          </label>
        </div>
      </div>

      <!-- 清空按钮 -->
      <div class="fixed bottom-14 left-0 right-0 bg-white border-t px-4 py-3 z-30" style="padding-bottom: calc(3rem + env(safe-area-inset-bottom));">
        <button 
          class="w-full h-11 rounded-lg bg-red-500 text-white font-medium"
          :disabled="!hasSelected"
          @click="confirmClear"
        >
          清空选中数据
        </button>
      </div>
    </div>

    <!-- 确认弹窗 -->
    <transition name="fade">
      <div v-if="showConfirm" class="fixed inset-0 bg-black/50 z-100 flex items-center justify-center">
        <div class="bg-white mx-4 rounded-lg p-4 w-full max-w-sm">
          <div class="flex items-center gap-2 mb-3">
            <span class="text-red-500 text-lg">⚠️</span>
            <h3 class="text-lg font-bold text-gray-800">确认清空</h3>
          </div>
          <p class="text-sm text-gray-600 mb-4">
            确定要清空选中的数据吗？此操作不可恢复！
          </p>
          <div class="flex gap-3">
            <button 
              class="flex-1 h-10 rounded-lg border border-gray-300 text-gray-700 font-medium"
              @click="showConfirm = false"
            >
              取消
            </button>
            <button 
              class="flex-1 h-10 rounded-lg bg-red-500 text-white font-medium"
              @click="clearData"
            >
              确认清空
            </button>
          </div>
        </div>
      </div>
    </transition>

    <!-- 成功提示 -->
    <transition name="fade">
      <div v-if="showSuccess" class="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-green-500 text-white px-6 py-3 rounded-lg text-sm z-100">
        数据清空成功！
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '../stores/cart'
import { useOrderStore } from '../stores/order'
import { useFavoritesStore } from '../stores/favorites'
import { useAddressStore } from '../stores/address'
import { useCouponStore } from '../stores/coupon'

const router = useRouter()
const cartStore = useCartStore()
const orderStore = useOrderStore()
const favoritesStore = useFavoritesStore()
const addressStore = useAddressStore()
const couponStore = useCouponStore()

const clearCart = ref(false)
const clearOrders = ref(false)
const clearFavorites = ref(false)
const clearAddresses = ref(false)
const clearCoupons = ref(false)
const clearAll = ref(false)
const showConfirm = ref(false)
const showSuccess = ref(false)

const cartCount = computed(() => cartStore.cartItems.length)
const orderCount = computed(() => orderStore.orders.length)
const favoriteCount = computed(() => favoritesStore.favorites.length)
const addressCount = computed(() => addressStore.addresses.length)
const couponCount = computed(() => couponStore.userCoupons.length)

const hasSelected = computed(() => {
  return clearCart.value || clearOrders.value || clearFavorites.value || 
         clearAddresses.value || clearCoupons.value
})

const handleSelectAll = () => {
  clearCart.value = clearAll.value
  clearOrders.value = clearAll.value
  clearFavorites.value = clearAll.value
  clearAddresses.value = clearAll.value
  clearCoupons.value = clearAll.value
}

const confirmClear = () => {
  if (!hasSelected.value) return
  showConfirm.value = true
}

const clearData = () => {
  if (clearCart.value) {
    cartStore.clearCart()
  }
  if (clearOrders.value) {
    orderStore.orders = []
    orderStore.saveToLocalStorage()
  }
  if (clearFavorites.value) {
    favoritesStore.favorites = []
    favoritesStore.saveToLocalStorage()
  }
  if (clearAddresses.value) {
    addressStore.addresses = []
    addressStore.saveToLocalStorage()
  }
  if (clearCoupons.value) {
    couponStore.userCoupons = []
    couponStore.saveToLocalStorage()
  }
  
  showConfirm.value = false
  showSuccess.value = true
  
  setTimeout(() => {
    showSuccess.value = false
    // 重置选择状态
    clearCart.value = false
    clearOrders.value = false
    clearFavorites.value = false
    clearAddresses.value = false
    clearCoupons.value = false
    clearAll.value = false
  }, 2000)
}

const goBack = () => {
  router.back()
}

onMounted(() => {
  // 初始化数据
  cartStore.loadFromLocalStorage()
  orderStore.orders = JSON.parse(localStorage.getItem('orders') || '[]')
  favoritesStore.loadFromLocalStorage()
  addressStore.loadFromLocalStorage()
  couponStore.loadFromLocalStorage()
})
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>