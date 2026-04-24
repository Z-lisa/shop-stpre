import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi } from '@/api/auth'

export const useUserStore = defineStore('user', () => {
  // 用户状态
  const token = ref(localStorage.getItem('token') || '')
  const userInfo = ref(JSON.parse(localStorage.getItem('userInfo') || 'null'))

  const isLoggedIn = computed(() => !!token.value)
  const isGuest = computed(() => !isLoggedIn.value)
  
  // VIP 会员相关计算属性
  const isVIP = computed(() => userInfo.value?.is_vip || false)
  const vipDiscount = computed(() => isVIP.value ? 0.85 : 1) // 会员 85 折
  const totalSpent = computed(() => parseFloat(userInfo.value?.total_spent || 0))
  const canBecomeVIP = computed(() => totalSpent.value >= 500 && !isVIP.value)

  const saveToLocalStorage = () => {
    if (token.value) {
      localStorage.setItem('token', token.value)
    } else {
      localStorage.removeItem('token')
    }
    
    if (userInfo.value) {
      localStorage.setItem('userInfo', JSON.stringify(userInfo.value))
    } else {
      localStorage.removeItem('userInfo')
    }
  }

  // 登录
  const login = async (username, password) => {
    const data = await authApi.login({ username, password })
    token.value = data.access_token
    userInfo.value = data.user
    saveToLocalStorage()
    return userInfo.value
  }

  // 注册
  const register = async (userData) => {
    const data = await authApi.register(userData)
    token.value = data.access_token
    userInfo.value = data.user
    saveToLocalStorage()
    return userInfo.value
  }

  // 获取用户信息
  const fetchUserInfo = async () => {
    if (!token.value) return null
    
    try {
      const data = await authApi.getCurrentUser()
      userInfo.value = data
      saveToLocalStorage()
      return data
    } catch (error) {
      console.error('获取用户信息失败:', error)
      return null
    }
  }

  // 更新用户信息
  const updateProfile = async (data) => {
    const updated = await authApi.updateProfile(data)
    userInfo.value = updated
    saveToLocalStorage()
    return updated
  }

  // 修改密码
  const changePassword = async (oldPassword, newPassword) => {
    await authApi.changePassword(oldPassword, newPassword)
  }

  // 退出登录
  const loginAsGuest = () => {
    token.value = ''
    userInfo.value = null
    saveToLocalStorage()
  }

  const logout = () => {
    token.value = ''
    userInfo.value = null
    saveToLocalStorage()
  }

  const init = async () => {
    if (token.value && !userInfo.value) {
      await fetchUserInfo()
    }
  }

  return {
    token,
    isLoggedIn,
    userInfo,
    isGuest,
    isVIP,
    vipDiscount,
    totalSpent,
    canBecomeVIP,
    login,
    register,
    fetchUserInfo,
    updateProfile,
    changePassword,
    loginAsGuest,
    logout,
    init
  }
})
