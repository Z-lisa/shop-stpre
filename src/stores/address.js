import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAddressStore = defineStore('address', () => {
  const addresses = ref(JSON.parse(localStorage.getItem('addresses') || '[]'))

  const saveToLocalStorage = () => {
    localStorage.setItem('addresses', JSON.stringify(addresses.value))
  }

  const defaultAddress = () => {
    return addresses.value.find(a => a.isDefault) || addresses.value[0] || null
  }

  const addAddress = (address) => {
    if (addresses.value.length === 0) {
      address.isDefault = true
    }
    addresses.value.push({
      id: 'addr_' + Date.now(),
      ...address
    })
    saveToLocalStorage()
  }

  const updateAddress = (id, newAddress) => {
    const index = addresses.value.findIndex(a => a.id === id)
    if (index > -1) {
      addresses.value[index] = { ...addresses.value[index], ...newAddress }
      saveToLocalStorage()
    }
  }

  const deleteAddress = (id) => {
    const index = addresses.value.findIndex(a => a.id === id)
    if (index > -1) {
      addresses.value.splice(index, 1)
      if (addresses.value.length > 0 && !addresses.value.some(a => a.isDefault)) {
        addresses.value[0].isDefault = true
      }
      saveToLocalStorage()
    }
  }

  const setDefault = (id) => {
    addresses.value.forEach(a => {
      a.isDefault = a.id === id
    })
    saveToLocalStorage()
  }

  const getAddressById = (id) => {
    return addresses.value.find(a => a.id === id)
  }

  if (addresses.value.length === 0) {
    addresses.value = [
      {
        id: 'addr_default',
        name: '张三',
        phone: '138****8888',
        province: '北京市',
        city: '北京市',
        district: '朝阳区',
        detail: '建国路xx号xx小区xx号楼xx单元xx室',
        isDefault: true
      }
    ]
    saveToLocalStorage()
  }

  return {
    addresses,
    defaultAddress,
    addAddress,
    updateAddress,
    deleteAddress,
    setDefault,
    getAddressById
  }
})
