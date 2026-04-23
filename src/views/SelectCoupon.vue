<template>
  <div class="min-h-screen bg-gray-50">
    <div class="bg-primary px-4 py-3">
      <div class="flex items-center gap-3">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" @click="goBack">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        <h1 class="text-white text-lg font-bold">选择优惠券</h1>
      </div>
    </div>

    <div class="p-4">
      <div 
        class="flex items-center justify-between p-4 bg-white border rounded-lg mb-3 cursor-pointer"
        :class="!selectedId ? 'border-primary bg-blue-50' : 'border-gray-200'"
        @click="selectCoupon(null)"
      >
        <span class="text-sm text-gray-700">不使用优惠券</span>
        <svg v-if="!selectedId" class="w-5 h-5 text-primary" fill="currentColor" viewBox="0 0 24 24">
          <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
        </svg>
      </div>
      
      <div v-if="couponStore.availableUserCoupons.length > 0" class="space-y-3">
        <div 
          v-for="coupon in couponStore.availableUserCoupons" 
          :key="coupon.id"
          class="flex rounded-lg overflow-hidden shadow-sm cursor-pointer bg-white"
          :class="selectedId === coupon.id ? 'ring-2 ring-primary' : ''"
          @click="selectCoupon(coupon)"
        >
          <div class="w-24 bg-gradient-to-br from-primary to-blue-600 flex flex-col items-center justify-center text-white p-2">
            <span class="text-xs">¥</span>
            <span class="text-2xl font-bold">{{ coupon.discount }}</span>
            <span class="text-xs opacity-80">{{ coupon.type === 'percentage' ? '折' : '' }}</span>
          </div>
          <div class="flex-1 p-3 flex items-center justify-between">
            <div>
              <h4 class="text-sm font-medium text-gray-800">{{ coupon.name }}</h4>
              <p class="text-xs text-gray-500 mt-1">{{ coupon.description }}</p>
              <p class="text-xs text-gray-400 mt-1">有效期至 {{ coupon.expireDate }}</p>
            </div>
            <svg v-if="selectedId === coupon.id" class="w-6 h-6 text-primary" fill="currentColor" viewBox="0 0 24 24">
              <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
            </svg>
          </div>
        </div>
      </div>
      
      <div v-else class="text-center py-10 text-gray-400 bg-white rounded-lg">
        暂无可用优惠券
        <button class="mt-2 text-primary text-sm block mx-auto" @click="goToCoupons">去领取</button>
      </div>
    </div>

    <div class="fixed bottom-0 left-0 right-0 bg-white border-t px-4 py-3">
      <button 
        class="w-full h-11 rounded-lg bg-primary text-white font-medium"
        @click="confirmSelect"
      >
        确认选择
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useCouponStore } from '../stores/coupon'

const router = useRouter()
const route = useRoute()
const couponStore = useCouponStore()

const selectedId = ref(null)
const from = ref('')

onMounted(() => {
  from.value = route.query.from || '/checkout'
  selectedId.value = route.query.selected || null
})

const selectCoupon = (coupon) => {
  selectedId.value = coupon?.id || null
}

const confirmSelect = () => {
  router.replace({
    path: from.value,
    query: { 
      ...route.query, 
      selectedCoupon: selectedId.value || '' 
    }
  })
}

const goToCoupons = () => {
  router.push('/coupons')
}

const goBack = () => {
  router.back()
}
</script>
