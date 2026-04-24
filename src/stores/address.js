import { defineStore } from 'pinia'
import { ref } from 'vue'
import { addressApi } from '@/api/address'

export const useAddressStore = defineStore('address', () => {
  const addresses = ref([])
  const loading = ref(false)

  // 获取地址列表
  const fetchAddresses = async () => {
    loading.value = true
    try {
      const data = await addressApi.getAddresses()
      addresses.value = data
      return data
    } catch (error) {
      console.error('获取地址列表失败:', error)
      addresses.value = []
      return []
    } finally {
      loading.value = false
    }
  }

  // 获取地址详情
  const fetchAddressDetail = async (addressId) => {
    loading.value = true
    try {
      const data = await addressApi.getAddressDetail(addressId)
      return data
    } catch (error) {
      console.error('获取地址详情失败:', error)
      return null
    } finally {
      loading.value = false
    }
  }

  // 新增地址
  const createAddress = async (data) => {
    const address = await addressApi.createAddress(data)
    await fetchAddresses()
    return address
  }

  // 更新地址
  const updateAddress = async (addressId, data) => {
    const address = await addressApi.updateAddress(addressId, data)
    await fetchAddresses()
    return address
  }

  // 删除地址
  const deleteAddress = async (addressId) => {
    await addressApi.deleteAddress(addressId)
    await fetchAddresses()
  }

  // 设为默认地址
  const setDefaultAddress = async (addressId) => {
    const address = await addressApi.setDefaultAddress(addressId)
    await fetchAddresses()
    return address
  }

  // 获取默认地址
  const getDefaultAddress = () => {
    return addresses.value.find(addr => addr.is_default) || null
  }

  // 别名，用于兼容 Checkout.vue 的调用
  const defaultAddress = getDefaultAddress

  // 根据ID获取地址
  const getAddressById = (addressId) => {
    return addresses.value.find(addr => addr.id === parseInt(addressId)) || null
  }

  // 别名，兼容 AddAddress.vue 的调用
  const addAddress = createAddress

  return {
    addresses,
    loading,
    fetchAddresses,
    fetchAddressDetail,
    createAddress,
    addAddress,
    updateAddress,
    deleteAddress,
    setDefaultAddress,
    getDefaultAddress,
    defaultAddress,
    getAddressById
  }
})
