import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCouponStore = defineStore('coupon', () => {
  const availableCoupons = ref([
    {
      id: 1,
      name: '新人专享券',
      discount: 10,
      minAmount: 59,
      type: 'fixed',
      expireDate: '2026-12-31',
      description: '满59元可用',
      status: 'available'
    },
    {
      id: 2,
      name: '满减优惠券',
      discount: 20,
      minAmount: 99,
      type: 'fixed',
      expireDate: '2026-06-30',
      description: '满99元可用',
      status: 'available'
    },
    {
      id: 3,
      name: '9折优惠券',
      discount: 0.9,
      minAmount: 0,
      type: 'percentage',
      expireDate: '2026-05-31',
      description: '全场通用9折',
      status: 'available'
    },
    {
      id: 4,
      name: '文学专区券',
      discount: 15,
      minAmount: 79,
      type: 'fixed',
      expireDate: '2026-04-30',
      description: '文学类购物满79元可用',
      status: 'available'
    }
  ])

  const userCoupons = ref(JSON.parse(localStorage.getItem('userCoupons') || '[]'))

  const saveToLocalStorage = () => {
    localStorage.setItem('userCoupons', JSON.stringify(userCoupons.value))
  }

  const claimCoupon = (couponId) => {
    const coupon = availableCoupons.value.find(c => c.id === couponId)
    if (coupon) {
      const newCoupon = {
        ...coupon,
        claimTime: new Date().toLocaleString('zh-CN'),
        used: false
      }
      userCoupons.value.push(newCoupon)
      saveToLocalStorage()
      return true
    }
    return false
  }

  const useCoupon = (couponId) => {
    const coupon = userCoupons.value.find(c => c.id === couponId)
    if (coupon && !coupon.used) {
      coupon.used = true
      coupon.useTime = new Date().toLocaleString('zh-CN')
      saveToLocalStorage()
      return true
    }
    return false
  }

  const availableUserCoupons = computed(() => {
    return userCoupons.value.filter(c => !c.used && new Date(c.expireDate) > new Date())
  })

  const usedUserCoupons = computed(() => {
    return userCoupons.value.filter(c => c.used)
  })

  const expiredUserCoupons = computed(() => {
    return userCoupons.value.filter(c => !c.used && new Date(c.expireDate) <= new Date())
  })

  const calculateDiscount = (coupon, totalPrice) => {
    if (!coupon) return 0
    if (totalPrice < coupon.minAmount) return 0
    
    if (coupon.type === 'fixed') {
      return Math.min(coupon.discount, totalPrice)
    } else if (coupon.type === 'percentage') {
      return totalPrice * (1 - coupon.discount)
    }
    return 0
  }

  return {
    availableCoupons,
    userCoupons,
    availableUserCoupons,
    usedUserCoupons,
    expiredUserCoupons,
    claimCoupon,
    useCoupon,
    calculateDiscount
  }
})
