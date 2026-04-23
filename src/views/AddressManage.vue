<template>
  <div class="min-h-screen bg-gray-50 pb-20">
    <div class="bg-primary px-4 pt-10 pb-3">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" @click="goBack">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
          <h1 class="text-white text-lg font-bold">地址管理</h1>
        </div>
        <button class="flex items-center gap-1 px-4 py-2 bg-white text-primary rounded-full text-sm font-medium" @click="goToAddAddress">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          新增地址
        </button>
      </div>
    </div>

    <div class="address-list px-4 py-4 space-y-3">
      <div 
        v-for="address in addressStore.addresses" 
        :key="address.id"
        class="bg-white rounded-lg p-4 shadow-sm"
        :class="address.isDefault ? 'border-2 border-primary' : ''"
      >
        <div class="flex items-start justify-between">
          <div class="flex-1">
            <div class="flex items-center gap-2 mb-1">
              <span class="font-medium text-gray-800">{{ address.name }}</span>
              <span class="text-gray-500">{{ address.phone }}</span>
              <span v-if="address.isDefault" class="px-2 py-0.5 bg-primary text-white text-xs rounded">默认</span>
            </div>
            <p class="text-sm text-gray-600">{{ address.province }}{{ address.city }}{{ address.district }}</p>
            <p class="text-sm text-gray-600">{{ address.detail }}</p>
          </div>
        </div>
        
        <div class="flex items-center justify-between mt-4 pt-3 border-t">
          <div class="flex items-center gap-2" @click="setDefault(address.id)">
            <div 
              class="w-5 h-5 rounded-full border-2 flex items-center justify-center"
              :class="address.isDefault ? 'border-primary bg-primary' : 'border-gray-300'"
            >
              <svg v-if="address.isDefault" class="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
            </div>
            <span class="text-sm text-gray-600">设为默认</span>
          </div>
          
          <div class="flex items-center gap-4">
            <button class="flex items-center gap-1 text-sm text-gray-500" @click="editAddress(address)">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
              编辑
            </button>
            <button class="flex items-center gap-1 text-sm text-gray-500" @click="deleteAddress(address.id)">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
              删除
            </button>
          </div>
        </div>
      </div>
    </div>

    <div v-if="addressStore.addresses.length === 0" class="empty-state flex flex-col items-center justify-center py-20">
      <svg class="w-20 h-20 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
      </svg>
      <p class="text-gray-400 mt-4">暂无收货地址</p>
      <button class="mt-4 px-6 py-2 bg-primary text-white rounded-full text-sm" @click="goToAddAddress">
        + 新增地址
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAddressStore } from '../stores/address'

const router = useRouter()
const addressStore = useAddressStore()

const goBack = () => {
  router.back()
}

const goToAddAddress = () => {
  router.push({
    path: '/add-address',
    query: { from: '/address' }
  })
}

const editAddress = (address) => {
  // 可以后续创建编辑地址页面，暂时使用新增页面逻辑
  router.push({
    path: '/add-address',
    query: { 
      from: '/address',
      edit: address.id 
    }
  })
}

const deleteAddress = (id) => {
  if (confirm('确定要删除这个地址吗？')) {
    addressStore.deleteAddress(id)
  }
}

const setDefault = (id) => {
  addressStore.setDefault(id)
}
</script>

<style scoped>
.safe-area-bottom {
  padding-bottom: env(safe-area-inset-bottom);
}
</style>
