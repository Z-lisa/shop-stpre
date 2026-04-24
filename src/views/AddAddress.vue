<template>
  <div class="min-h-screen bg-gray-50 pb-32">
    <div class="bg-primary px-4 py-3">
      <div class="flex items-center gap-3">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" @click="goBack">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        <h1 class="text-white text-lg font-bold">{{ isEdit ? '编辑收货地址' : '新增收货地址' }}</h1>
      </div>
    </div>

    <div class="p-4 space-y-4">
      <div>
        <label class="text-xs text-gray-500">收货人</label>
        <input 
          v-model="form.name" 
          type="text" 
          class="w-full mt-1 p-3 border rounded-lg text-sm bg-white" 
          placeholder="请输入收货人姓名" 
        />
      </div>
      <div>
        <label class="text-xs text-gray-500">手机号</label>
        <input 
          v-model="form.phone" 
          type="tel" 
          class="w-full mt-1 p-3 border rounded-lg text-sm bg-white" 
          placeholder="请输入手机号" 
        />
      </div>
      <div class="grid grid-cols-3 gap-2">
        <div>
          <label class="text-xs text-gray-500">省份</label>
          <input 
            v-model="form.province" 
            type="text" 
            class="w-full mt-1 p-3 border rounded-lg text-sm bg-white" 
            placeholder="省" 
          />
        </div>
        <div>
          <label class="text-xs text-gray-500">城市</label>
          <input 
            v-model="form.city" 
            type="text" 
            class="w-full mt-1 p-3 border rounded-lg text-sm bg-white" 
            placeholder="市" 
          />
        </div>
        <div>
          <label class="text-xs text-gray-500">区县</label>
          <input 
            v-model="form.district" 
            type="text" 
            class="w-full mt-1 p-3 border rounded-lg text-sm bg-white" 
            placeholder="区" 
          />
        </div>
      </div>
      <div>
        <label class="text-xs text-gray-500">详细地址</label>
        <input 
          v-model="form.detail" 
          type="text" 
          class="w-full mt-1 p-3 border rounded-lg text-sm bg-white" 
          placeholder="街道、楼栋、门牌号" 
        />
      </div>
      <div class="flex items-center gap-2 pt-2">
        <input 
          v-model="form.isDefault" 
          type="checkbox" 
          id="isDefault"
          class="w-4 h-4"
        />
        <label for="isDefault" class="text-sm text-gray-700">设为默认地址</label>
      </div>
    </div>

    <div class="fixed bottom-14 left-0 right-0 bg-white border-t px-4 py-3 z-30" style="padding-bottom: calc(0.75rem + env(safe-area-inset-bottom));">
      <button 
        class="w-full h-11 rounded-lg bg-primary text-white font-medium"
        @click="saveAddress"
      >
        保存地址
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAddressStore } from '../stores/address'

const router = useRouter()
const route = useRoute()
const addressStore = useAddressStore()

const editId = ref(route.query.edit || null)
const isEdit = computed(() => !!editId.value)

const form = ref({
  name: '',
  phone: '',
  province: '',
  city: '',
  district: '',
  detail: '',
  isDefault: false
})

onMounted(() => {
  if (isEdit.value) {
    const address = addressStore.getAddressById(editId.value)
    if (address) {
      form.value = { ...address }
    }
  }
})

const saveAddress = () => {
  if (!form.value.name || !form.value.phone || !form.value.detail) {
    alert('请填写完整信息')
    return
  }
  
  if (isEdit.value) {
    addressStore.updateAddress(editId.value, form.value)
  } else {
    addressStore.addAddress(form.value)
  }
  
  // 获取返回页面
  const from = route.query.from || '/address'
  
  // 如果是从选择地址页面来的，返回到选择页面
  if (from === '/select-address') {
    if (isEdit.value) {
      router.replace({
        path: from,
        query: { 
          ...route.query,
          selected: editId.value 
        }
      })
    } else {
      const newAddress = addressStore.addresses[addressStore.addresses.length - 1]
      router.replace({
        path: from,
        query: { 
          ...route.query,
          selected: newAddress.id 
        }
      })
    }
  } else {
    router.replace(from)
  }
}

const goBack = () => {
  router.back()
}
</script>
