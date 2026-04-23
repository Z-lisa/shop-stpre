<template>
  <div class="min-h-screen bg-gray-50 pb-20">
    <div class="bg-primary px-4 pt-10 pb-3">
      <div class="flex items-center gap-3">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" @click="goBack">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        <h1 class="text-white text-lg font-bold">优惠券</h1>
      </div>
    </div>

    <div class="coupon-tabs bg-white flex overflow-x-auto border-b sticky top-0 z-10">
      <div 
        v-for="tab in tabs" 
        :key="tab.value"
        class="flex-shrink-0 px-6 py-3 text-sm font-medium transition-colors cursor-pointer"
        :class="activeTab === tab.value ? 'text-primary border-b-2 border-primary' : 'text-gray-500'"
        @click="activeTab = tab.value"
      >
        {{ tab.label }}
      </div>
    </div>

    <div class="p-4">
      <template v-if="activeTab === 'available'">
        <div v-if="couponStore.availableCoupons.length > 0" class="space-y-4">
          <div 
            v-for="coupon in couponStore.availableCoupons" 
            :key="coupon.id"
            class="bg-white rounded-lg overflow-hidden shadow-sm"
          >
            <div class="flex">
              <div class="w-28 bg-gradient-to-br from-primary to-blue-600 flex flex-col items-center justify-center text-white p-3">
                <span class="text-xs">¥</span>
                <span class="text-3xl font-bold">{{ coupon.discount }}</span>
                <span class="text-xs mt-1 opacity-80">{{ coupon.type === 'percentage' ? '折' : '' }}</span>
              </div>
              <div class="flex-1 p-4">
                <h3 class="font-medium text-gray-800">{{ coupon.name }}</h3>
                <p class="text-xs text-gray-500 mt-1">{{ coupon.description }}</p>
                <p class="text-xs text-gray-400 mt-2">有效期至 {{ coupon.expireDate }}</p>
              </div>
              <div class="flex flex-col items-center justify-center pr-4">
                <button 
                  v-if="!isClaimed(coupon.id)"
                  class="px-4 py-1.5 bg-primary text-white text-sm rounded-full"
                  @click="handleClaim(coupon)"
                >
                  立即领取
                </button>
                <span v-else class="px-4 py-1.5 bg-gray-200 text-gray-400 text-sm rounded-full">
                  已领取
                </span>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="text-center py-20 text-gray-400">
          暂无可用优惠券
        </div>
      </template>

      <template v-else-if="activeTab === 'my'">
        <div v-if="couponStore.availableUserCoupons.length > 0" class="space-y-4">
          <div 
            v-for="coupon in couponStore.availableUserCoupons" 
            :key="coupon.id"
            class="bg-white rounded-lg overflow-hidden shadow-sm"
          >
            <div class="flex">
              <div class="w-28 bg-gradient-to-br from-primary to-blue-600 flex flex-col items-center justify-center text-white p-3">
                <span class="text-xs">¥</span>
                <span class="text-3xl font-bold">{{ coupon.discount }}</span>
                <span class="text-xs mt-1 opacity-80">{{ coupon.type === 'percentage' ? '折' : '' }}</span>
              </div>
              <div class="flex-1 p-4">
                <h3 class="font-medium text-gray-800">{{ coupon.name }}</h3>
                <p class="text-xs text-gray-500 mt-1">{{ coupon.description }}</p>
                <p class="text-xs text-gray-400 mt-2">有效期至 {{ coupon.expireDate }}</p>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="text-center py-20 text-gray-400">
          暂无优惠券，去领取吧~
        </div>
      </template>

      <template v-else-if="activeTab === 'used'">
        <div v-if="couponStore.usedUserCoupons.length > 0" class="space-y-4">
          <div 
            v-for="coupon in couponStore.usedUserCoupons" 
            :key="coupon.id"
            class="bg-white rounded-lg overflow-hidden shadow-sm opacity-60"
          >
            <div class="flex">
              <div class="w-28 bg-gray-300 flex flex-col items-center justify-center text-white p-3">
                <span class="text-xs">¥</span>
                <span class="text-3xl font-bold">{{ coupon.discount }}</span>
                <span class="text-xs mt-1 opacity-80">{{ coupon.type === 'percentage' ? '折' : '' }}</span>
              </div>
              <div class="flex-1 p-4">
                <h3 class="font-medium text-gray-800">{{ coupon.name }}</h3>
                <p class="text-xs text-gray-500 mt-1">{{ coupon.description }}</p>
                <p class="text-xs text-gray-400 mt-2">已使用</p>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="text-center py-20 text-gray-400">
          暂无已使用优惠券
        </div>
      </template>
    </div>

    <transition name="fade">
      <div v-if="showToast" class="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-gray-800 text-white px-6 py-3 rounded-lg text-sm z-100">
        {{ toastMessage }}
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCouponStore } from '../stores/coupon'

const router = useRouter()
const couponStore = useCouponStore()

const activeTab = ref('available')
const showToast = ref(false)
const toastMessage = ref('')

const tabs = [
  { label: '领券中心', value: 'available' },
  { label: '我的优惠券', value: 'my' },
  { label: '已使用', value: 'used' }
]

const goBack = () => {
  router.back()
}

const isClaimed = (couponId) => {
  return couponStore.userCoupons.some(c => c.id === couponId)
}

const handleClaim = (coupon) => {
  if (couponStore.claimCoupon(coupon.id)) {
    showToastMessage('领取成功')
  }
}

const showToastMessage = (message) => {
  toastMessage.value = message
  showToast.value = true
  setTimeout(() => {
    showToast.value = false
  }, 1500)
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
