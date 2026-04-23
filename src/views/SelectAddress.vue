<template>
  <div class="min-h-screen bg-gray-50">
    <div class="bg-primary px-4 py-3">
      <div class="flex items-center gap-3">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" @click="goBack">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        <h1 class="text-white text-lg font-bold">选择收货地址</h1>
      </div>
    </div>

    <div class="p-4 space-y-3">
      <div 
        v-for="addr in addressStore.addresses" 
        :key="addr.id"
        class="p-4 bg-white border rounded-lg"
        :class="selectedId === addr.id ? 'border-primary bg-blue-50' : 'border-gray-200'"
        @click="selectAddress(addr.id)"
      >
        <div class="flex justify-between items-start">
          <div>
            <p class="text-sm font-medium text-gray-800">{{ addr.name }} {{ addr.phone }}</p>
            <p class="text-xs text-gray-500 mt-1">{{ addr.province }}{{ addr.city }}{{ addr.district }} {{ addr.detail }}</p>
          </div>
          <span v-if="addr.isDefault" class="text-xs text-primary">默认</span>
        </div>
      </div>

      <button class="w-full p-4 bg-white border border-dashed border-gray-300 rounded-lg text-primary text-sm" @click="goToAddAddress">
        + 新增收货地址
      </button>
    </div>

    <div class="fixed bottom-0 left-0 right-0 bg-white border-t px-4 py-3">
      <button 
        class="w-full h-11 rounded-lg bg-primary text-white font-medium"
        :disabled="!selectedId"
        :class="!selectedId ? 'opacity-50' : ''"
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
import { useAddressStore } from '../stores/address'

const router = useRouter()
const route = useRoute()
const addressStore = useAddressStore()

const selectedId = ref('')
const from = ref('')

onMounted(() => {
  // 获取来源页面和已选地址
  from.value = route.query.from || '/checkout'
  selectedId.value = route.query.selected || ''
  
  // 如果没有预选地址，使用默认地址
  if (!selectedId.value) {
    const defaultAddr = addressStore.defaultAddress()
    if (defaultAddr) {
      selectedId.value = defaultAddr.id
    }
  }
})

const selectAddress = (id) => {
  selectedId.value = id
}

const confirmSelect = () => {
  // 返回结算页，传递选中的地址ID
  router.replace({
    path: from.value,
    query: { ...route.query, selectedAddress: selectedId.value }
  })
}

const goToAddAddress = () => {
  router.push({
    path: '/add-address',
    query: { 
      from: '/select-address',
      ...route.query
    }
  })
}

const goBack = () => {
  router.back()
}
</script>
