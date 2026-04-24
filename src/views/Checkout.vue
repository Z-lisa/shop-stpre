<template>
  <div class="min-h-screen bg-gray-50 pb-24">
    <div class="bg-primary px-4 py-3">
      <div class="flex items-center gap-3">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" @click="goBack">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        <h1 class="text-white text-lg font-bold">确认订单</h1>
      </div>
    </div>

    <div class="address-section bg-white px-4 py-4 mt-2" @click="goToSelectAddress">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3 flex-1">
          <span class="text-xl">📍</span>
          <div class="flex-1">
            <p class="text-sm font-medium text-gray-800">{{ selectedAddress?.name }} {{ selectedAddress?.phone }}</p>
            <p class="text-xs text-gray-500 mt-1">{{ selectedAddress?.province }}{{ selectedAddress?.city }}{{ selectedAddress?.district }} {{ selectedAddress?.detail }}</p>
          </div>
        </div>
        <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
        </svg>
      </div>
    </div>

    <div class="order-items bg-white px-4 py-4 mt-2">
      <h2 class="text-sm font-bold text-gray-800 mb-3">商品清单</h2>
      <div 
        v-for="item in editableItems" 
        :key="item.id"
        class="order-item flex items-center gap-3 py-3 border-b border-gray-100 last:border-0"
      >
        <img :src="item.cover" :alt="item.name" class="w-16 h-20 object-cover rounded" />
        <div class="flex-1">
          <h3 class="text-sm font-medium text-gray-800 truncate">{{ item.name }}</h3>
          <p class="text-xs text-gray-500 mt-1">{{ item.author }}</p>
          <div class="flex items-center justify-between mt-2">
            <span class="text-sm text-primary font-bold">¥{{ item.price }}</span>
            <div class="flex items-center border rounded-lg">
              <button 
                class="w-8 h-8 flex items-center justify-center text-gray-600"
                @click="decreaseQty(item)"
              >-</button>
              <span class="w-8 text-center text-sm text-gray-800">{{ item.quantity }}</span>
              <button 
                class="w-8 h-8 flex items-center justify-center text-gray-600"
                @click="increaseQty(item)"
              >+</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="coupon-section bg-white px-4 py-4 mt-2" @click="goToSelectCoupon">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <span class="text-xl">🎫</span>
          <span class="text-sm text-gray-700">优惠券</span>
        </div>
        <div class="flex items-center gap-2">
          <span v-if="selectedCoupon" class="text-sm text-primary">{{ selectedCoupon.name }}</span>
          <span v-else class="text-sm text-gray-400">{{ couponStore.availableUserCoupons.length }}张可用</span>
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </div>
      </div>
    </div>

    <div class="order-notes bg-white px-4 py-4 mt-2">
      <h2 class="text-sm font-bold text-gray-800 mb-3">订单备注</h2>
      <textarea 
        v-model="orderNote" 
        class="w-full p-3 border border-gray-200 rounded-lg text-sm resize-none" 
        placeholder="请输入订单备注（如：配送时间要求、包装要求等）"
        rows="3"
        maxlength="200"
      ></textarea>
      <div class="flex justify-between text-xs text-gray-400 mt-1">
        <span>最多200字</span>
        <span>{{ orderNote.length }}/200</span>
      </div>
    </div>

    <div class="order-summary bg-white px-4 py-4 mt-2">
      <h2 class="text-sm font-bold text-gray-800 mb-3">订单金额</h2>
      <div class="space-y-2">
        <div class="flex justify-between text-sm">
          <span class="text-gray-500">商品金额</span>
          <span class="text-gray-800">¥{{ totalPrice.toFixed(2) }}</span>
        </div>
        <div class="flex justify-between text-sm">
          <span class="text-gray-500">运费</span>
          <span class="text-gray-800">¥0.00</span>
        </div>
        <div v-if="userStore.isVIP" class="flex justify-between text-sm">
          <span class="text-gray-500">VIP会员折扣 (85折)</span>
          <span class="text-price-orange">-¥{{ vipDiscountAmount.toFixed(2) }}</span>
        </div>
        <div v-if="discount > 0" class="flex justify-between text-sm pt-2 border-t">
          <span class="text-gray-500">优惠券</span>
          <span class="text-price-orange">-¥{{ discount.toFixed(2) }}</span>
        </div>
        <div class="flex justify-between text-base pt-2 border-t">
          <span class="font-medium text-gray-800">实付金额</span>
          <span class="text-primary font-bold">¥{{ finalPrice.toFixed(2) }}</span>
        </div>
        <div v-if="userStore.canBecomeVIP" class="text-xs text-orange-500 bg-orange-50 p-2 rounded mt-2">
          💎 您已消费¥{{ userStore.totalSpent.toFixed(2) }}，再消费¥{{ (500 - userStore.totalSpent).toFixed(2) }}即可成为VIP会员享受85折优惠！
        </div>
      </div>
    </div>

    <div class="fixed bottom-14 left-0 right-0 bg-white border-t px-4 py-3 z-30" style="padding-bottom: calc(3rem + env(safe-area-inset-bottom));">
      <button 
        class="w-full h-11 rounded-lg bg-primary text-white font-medium"
        @click="handleSubmitOrder"
      >
        提交订单
      </button>
    </div>

    <PayModal 
      :show="showPayModal" 
      :total-price="finalPrice"
      :order-id="createdOrderId"
      @close="handlePayModalClose"
      @success="handlePaySuccess"
    />

    <transition name="fade">
      <div v-if="showToast" class="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-gray-800 text-white px-6 py-3 rounded-lg text-sm z-100">
        {{ toastMessage }}
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useCartStore } from '../stores/cart'
import { useAddressStore } from '../stores/address'
import { useOrderStore } from '../stores/order'
import { useCouponStore } from '../stores/coupon'
import { useUserStore } from '../stores/user'
import PayModal from '../components/PayModal.vue'

const router = useRouter()
const route = useRoute()
const cartStore = useCartStore()
const addressStore = useAddressStore()
const orderStore = useOrderStore()
const couponStore = useCouponStore()
const userStore = useUserStore()

const showPayModal = ref(false)
const showToast = ref(false)
const toastMessage = ref('')
const createdOrderId = ref('')
const selectedAddressId = ref('')
const selectedCouponId = ref(null)
const orderNote = ref('')

const selectedAddress = computed(() => {
  return addressStore.addresses.find(a => a.id === selectedAddressId.value) || addressStore.defaultAddress()
})

const selectedCoupon = computed(() => {
  return couponStore.userCoupons.find(c => c.id === selectedCouponId.value)
})

const editableItems = computed(() => {
  return cartStore.getSelectedItems()
})

const totalPrice = computed(() => {
  return editableItems.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
})

const vipDiscountAmount = computed(() => {
  if (!userStore.isVIP) return 0
  return totalPrice.value * (1 - userStore.vipDiscount)
})

const priceAfterVipDiscount = computed(() => {
  return userStore.isVIP ? totalPrice.value * userStore.vipDiscount : totalPrice.value
})

const discount = computed(() => {
  if (!selectedCoupon.value) return 0
  return couponStore.calculateDiscount(selectedCoupon.value, priceAfterVipDiscount.value)
})

const finalPrice = computed(() => {
  return Math.max(0, priceAfterVipDiscount.value - discount.value)
})

const decreaseQty = (item) => {
  if (item.quantity > 1) {
    item.quantity--
    cartStore.updateQuantity(item.id, item.quantity)
  }
}

const increaseQty = (item) => {
  if (item.quantity < 99) {
    item.quantity++
    cartStore.updateQuantity(item.id, item.quantity)
  }
}

const goToSelectAddress = () => {
  router.push({
    path: '/select-address',
    query: { 
      from: '/checkout',
      selected: selectedAddressId.value 
    }
  })
}

const goToSelectCoupon = () => {
  router.push({
    path: '/select-coupon',
    query: { 
      from: '/checkout',
      selected: selectedCouponId.value || '' 
    }
  })
}

const goBack = () => {
  router.back()
}

const handleSubmitOrder = () => {
  if (!userStore.isLoggedIn) {
    showToastMessage('请先登录后再下单')
    return
  }
  if (!selectedAddress.value) {
    showToastMessage('请选择收货地址')
    return
  }
  if (editableItems.value.length === 0) {
    showToastMessage('请选择商品')
    return
  }

  createdOrderId.value = orderStore.createOrder({
    items: [...editableItems.value],
    totalPrice: totalPrice.value,
    address: selectedAddress.value,
    coupon: selectedCoupon.value,
    note: orderNote.value
  })

  showPayModal.value = true
}

const handlePaySuccess = (data) => {
  // 支付成功后从购物车删除商品
  editableItems.value.forEach(item => {
    cartStore.removeFromCart(item.id)
  })
  
  // 支付成功后使用优惠券
  if (selectedCoupon.value) {
    couponStore.useCoupon(selectedCoupon.value.id)
  }
  
  orderStore.payOrder(data.orderId, data.method)
  router.replace({
    path: '/order-success',
    query: { orderId: data.orderId }
  })
}

const handlePayModalClose = () => {
  showPayModal.value = false
  // 如果支付弹窗关闭，需要删除已创建的订单（如果支付未成功）
  if (createdOrderId.value) {
    const order = orderStore.getOrderById(createdOrderId.value)
    if (order && order.status === 'pending') {
      // 删除未支付的订单
      const index = orderStore.orders.findIndex(o => o.id === createdOrderId.value)
      if (index > -1) {
        orderStore.orders.splice(index, 1)
        orderStore.saveToLocalStorage()
      }
    }
  }
  createdOrderId.value = ''
}

const showToastMessage = (message) => {
  toastMessage.value = message
  showToast.value = true
  setTimeout(() => {
    showToast.value = false
  }, 1500)
}

onMounted(() => {
  // 从路由参数获取选中的地址
  if (route.query.selectedAddress) {
    selectedAddressId.value = route.query.selectedAddress
  } else {
    const defaultAddr = addressStore.defaultAddress()
    if (defaultAddr) {
      selectedAddressId.value = defaultAddr.id
    }
  }
  
  // 从路由参数获取选中的优惠券
  if (route.query.selectedCoupon) {
    selectedCouponId.value = route.query.selectedCoupon
  }
  
  if (editableItems.value.length === 0) {
    router.replace('/cart')
  }
})
</script>
