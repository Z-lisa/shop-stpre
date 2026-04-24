<template>
  <div class="min-h-screen bg-gray-50 pb-24">
    <div class="bg-primary px-4 py-3">
      <h1 class="text-white text-lg font-bold">购物车</h1>
    </div>

    <div v-if="cartStore.cartItems.length > 0" class="cart-content">
      <div class="bg-white px-4 py-3 flex items-center justify-between border-b">
        <div class="flex items-center" @click="cartStore.selectAll">
          <div 
            class="w-5 h-5 rounded border-2 flex items-center justify-center mr-2 transition-colors"
            :class="cartStore.isAllSelected ? 'border-primary bg-primary' : 'border-gray-300'"
          >
            <svg v-if="cartStore.isAllSelected" class="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
          </div>
          <span class="text-sm text-gray-700">全选</span>
        </div>
        <span class="text-sm text-gray-500">共{{ cartStore.totalItems }}件商品</span>
      </div>

      <div class="cart-list">
        <div 
          v-for="item in cartStore.cartItems" 
          :key="item.id"
          class="cart-item bg-white px-4 py-3 flex items-start gap-3 border-b"
        >
          <div 
            class="w-5 h-5 rounded border-2 flex items-center justify-center mt-2 transition-colors flex-shrink-0"
            :class="cartStore.selectedItems.includes(item.id) ? 'border-primary bg-primary' : 'border-gray-300'"
            @click="cartStore.toggleSelect(item.id)"
          >
            <svg v-if="cartStore.selectedItems.includes(item.id)" class="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
          </div>

          <img :src="item.cover" :alt="item.name" class="w-20 h-24 object-cover rounded flex-shrink-0" />

          <div class="flex-1 min-w-0">
            <div class="flex justify-between items-start">
              <h3 class="text-sm font-medium text-gray-800 truncate flex-1">{{ item.name }}</h3>
              <button class="text-gray-400 ml-2 flex-shrink-0" @click="handleDelete(item.id)">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
            <p class="text-xs text-gray-500 mt-1 truncate">{{ item.author }}</p>
            <p v-if="item.size" class="text-xs text-gray-400 mt-1">尺码: {{ item.size }}</p>
            <div class="flex items-center justify-between mt-2">
              <span class="text-sm text-primary font-bold">¥{{ item.price }}</span>
              <div class="flex items-center border rounded-lg">
                <button 
                  class="w-8 h-8 flex items-center justify-center text-gray-600"
                  @click="updateQty(item.id, item.quantity - 1)"
                >-</button>
                <span class="w-8 text-center text-sm text-gray-800">{{ item.quantity }}</span>
                <button 
                  class="w-8 h-8 flex items-center justify-center text-gray-600"
                  @click="updateQty(item.id, item.quantity + 1)"
                >+</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="fixed bottom-14 left-0 right-0 bg-white border-t px-4 py-3 flex items-center justify-between z-30" style="padding-bottom: calc(3rem + env(safe-area-inset-bottom));">
        <div>
          <div class="flex items-center gap-1">
            <span class="text-sm text-gray-500">合计:</span>
            <span class="text-lg text-primary font-bold">¥{{ cartStore.selectedTotal.toFixed(2) }}</span>
          </div>
          <p class="text-xs text-gray-400">已选{{ cartStore.selectedCount }}件</p>
        </div>
        <button 
          class="h-11 px-8 rounded-lg font-medium transition-colors"
          :class="cartStore.selectedCount > 0 ? 'bg-primary text-white' : 'bg-gray-300 text-gray-500'"
          :disabled="cartStore.selectedCount === 0"
          @click="handleCheckout"
        >
          结算
        </button>
      </div>
    </div>

    <div v-else class="empty-cart flex flex-col items-center justify-center py-20">
      <svg class="w-24 h-24 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
      </svg>
      <p class="text-gray-400 mt-4">购物车空空如也</p>
      <button class="mt-4 px-6 py-2 bg-primary text-white rounded-lg text-sm" @click="goShopping">
        去逛逛
      </button>
    </div>

    <!-- 购物车商品推荐 -->
    <div v-if="recommendProducts.length > 0" class="mt-2 bg-white px-4 py-3">
      <div class="flex items-center justify-between mb-3">
        <span class="text-sm font-medium text-gray-700">猜你喜欢</span>
        <span class="text-xs text-gray-400">根据您的购物车推荐</span>
      </div>
      <div class="grid grid-cols-2 gap-3">
        <div 
          v-for="product in recommendProducts" 
          :key="product.id"
          class="text-center cursor-pointer"
          @click="router.push(`/book/${product.id}`)"
        >
          <img :src="product.cover" :alt="product.name" class="w-full h-28 object-cover rounded" />
          <p class="text-xs text-gray-700 mt-2 line-clamp-2">{{ product.name }}</p>
          <p class="text-xs text-primary font-bold mt-1">¥{{ product.price }}</p>
          <button 
            class="mt-1 px-2 py-1 bg-primary text-white text-xs rounded w-full"
            @click.stop="handleAddToCart(product)"
          >
            加入购物车
          </button>
        </div>
      </div>
    </div>

    <transition name="fade">
      <div v-if="showToast" class="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-gray-800 text-white px-6 py-3 rounded-lg text-sm z-100">
        {{ toastMessage }}
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '../stores/cart'
import { useUserStore } from '../stores/user'
import { products } from '../data/books'

const router = useRouter()
const cartStore = useCartStore()
const userStore = useUserStore()

const showToast = ref(false)
const toastMessage = ref('')

const recommendProducts = computed(() => {
  const cartProductIds = cartStore.cartItems.map(item => item.id)
  
  // 排除购物车中已有的商品
  const availableProducts = products.filter(product => !cartProductIds.includes(product.id))
  
  // 简单推荐逻辑：按评分和销量排序，取前4个
  return availableProducts
    .sort((a, b) => {
      const scoreA = a.rating * 0.6 + (a.sales || 0) * 0.4
      const scoreB = b.rating * 0.6 + (b.sales || 0) * 0.4
      return scoreB - scoreA
    })
    .slice(0, 4)
})

const updateQty = (id, quantity) => {
  if (quantity < 1) {
    handleDelete(id)
  } else {
    cartStore.updateQuantity(id, Math.min(99, quantity))
  }
}

const handleDelete = (id) => {
  cartStore.removeFromCart(id)
  showToastMessage('已删除')
}

const handleCheckout = () => {
  if (!userStore.isLoggedIn) {
    showToastMessage('请先登录后再下单')
    return
  }
  if (cartStore.selectedCount > 0) {
    router.push('/checkout')
  }
}

const goShopping = () => {
  router.push('/')
}

const handleAddToCart = (product) => {
  if (!userStore.isLoggedIn) {
    showToastMessage('请先登录后再加入购物车')
    return
  }
  cartStore.addToCart(product, 1)
  showToastMessage('已加入购物车')
}

const showToastMessage = (message) => {
  toastMessage.value = message
  showToast.value = true
  setTimeout(() => {
    showToast.value = false
  }, 1500)
}
</script>
