import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  // 从 localStorage 读取登录状态
  const isLoggedIn = ref(JSON.parse(localStorage.getItem('isLoggedIn') || 'false'))
  const userInfo = ref(JSON.parse(localStorage.getItem('userInfo') || 'null'))

  const isGuest = computed(() => !isLoggedIn.value)
  
  // VIP会员相关计算属性
  const isVIP = computed(() => userInfo.value?.isVIP || false)
  const vipDiscount = computed(() => isVIP.value ? 0.85 : 1) // 会员85折
  const totalSpent = computed(() => userInfo.value?.totalSpent || 0)
  const canBecomeVIP = computed(() => totalSpent.value >= 500 && !isVIP.value)

  const saveToLocalStorage = () => {
    localStorage.setItem('isLoggedIn', JSON.stringify(isLoggedIn.value))
    localStorage.setItem('userInfo', JSON.stringify(userInfo.value))
  }

  // 登录
  const login = (userData) => {
    isLoggedIn.value = true
    userInfo.value = {
      id: 'user_' + Date.now(),
      name: userData.name || '用户' + Math.floor(Math.random() * 10000),
      avatar: userData.avatar || '',
      phone: userData.phone || '',
      totalSpent: 0,
      isVIP: false,
      vipSince: null,
      ...userData
    }
    saveToLocalStorage()
    return userInfo.value
  }

  // 游客登录（不保存订单）
  const loginAsGuest = () => {
    isLoggedIn.value = false
    userInfo.value = {
      id: 'guest_' + Date.now(),
      name: '游客',
      isGuest: true
    }
    saveToLocalStorage()
  }

  // 退出登录
  const logout = () => {
    isLoggedIn.value = false
    userInfo.value = null
    localStorage.removeItem('isLoggedIn')
    localStorage.removeItem('userInfo')
    // 清除游客订单数据
    localStorage.removeItem('orders')
  }

  // 更新消费金额
  const updateSpending = (amount) => {
    if (isLoggedIn.value && userInfo.value) {
      userInfo.value.totalSpent = (userInfo.value.totalSpent || 0) + amount
      
      // 检查是否满足VIP条件
      if (userInfo.value.totalSpent >= 500 && !userInfo.value.isVIP) {
        userInfo.value.isVIP = true
        userInfo.value.vipSince = new Date().toISOString()
      }
      
      saveToLocalStorage()
    }
  }

  // 手动升级为VIP（用于测试）
  const upgradeToVIP = () => {
    if (isLoggedIn.value && userInfo.value) {
      userInfo.value.isVIP = true
      userInfo.value.vipSince = new Date().toISOString()
      saveToLocalStorage()
    }
  }

  // 初始化
  if (!isLoggedIn.value && !userInfo.value) {
    loginAsGuest()
  }

  return {
    isLoggedIn,
    userInfo,
    isGuest,
    isVIP,
    vipDiscount,
    totalSpent,
    canBecomeVIP,
    login,
    loginAsGuest,
    logout,
    updateSpending,
    upgradeToVIP
  }
})
