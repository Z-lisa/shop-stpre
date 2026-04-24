import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { couponApi } from '@/api/coupon'

export const useCouponStore = defineStore('coupon', () => {
  const coupons = ref([])
  const myCoupons = ref([])
  const loading = ref(false)

  // 别名，兼容 Checkout.vue
  const userCoupons = myCoupons

  // 可领取的优惠券（领券中心）
  const availableCoupons = computed(() => {
    return coupons.value.filter(c => {
      // 过滤掉已领取的
      const claimed = myCoupons.value.some(mc => mc.coupon_id === c.id || mc.id === c.id)
      return !claimed
    })
  })

  // 可用的优惠券（未使用）
  const availableUserCoupons = computed(() => {
    return myCoupons.value.filter(c => c.status === 'unused' || !c.status)
  })

  // 已使用的优惠券
  const usedUserCoupons = computed(() => {
    return myCoupons.value.filter(c => c.status === 'used')
  })

  // 计算折扣金额
  const calculateDiscount = (coupon, price) => {
    if (!coupon) return 0
    if (coupon.type === 'percentage') {
      return price * (1 - coupon.value)
    } else if (coupon.type === 'fixed') {
      return coupon.value
    }
    return 0
  }

  // 获取优惠券列表
  const fetchCoupons = async () => {
    loading.value = true
    try {
      const data = await couponApi.getCoupons()
      coupons.value = data
      return data
    } catch (error) {
      console.error('获取优惠券列表失败:', error)
      coupons.value = []
      return []
    } finally {
      loading.value = false
    }
  }

  // 领取优惠券
  const claimCoupon = async (couponId) => {
    await couponApi.claimCoupon(couponId)
    await fetchMyCoupons()
  }

  // 获取我的优惠券
  const fetchMyCoupons = async () => {
    loading.value = true
    try {
      const data = await couponApi.getMyCoupons()
      myCoupons.value = data
      return data
    } catch (error) {
      console.error('获取我的优惠券失败:', error)
      myCoupons.value = []
      return []
    } finally {
      loading.value = false
    }
  }

  // 获取可用优惠券
  const fetchAvailableCoupons = async () => {
    loading.value = true
    try {
      const data = await couponApi.getAvailableCoupons()
      myCoupons.value = data
      return data
    } catch (error) {
      console.error('获取可用优惠券失败:', error)
      myCoupons.value = []
      return []
    } finally {
      loading.value = false
    }
  }

  // 使用优惠券
  const useCoupon = (couponId) => {
    const coupon = myCoupons.value.find(c => c.id === couponId)
    if (coupon) {
      coupon.status = 'used'
    }
  }

  return {
    coupons,
    myCoupons,
    userCoupons,
    availableCoupons,
    availableUserCoupons,
    usedUserCoupons,
    loading,
    fetchCoupons,
    claimCoupon,
    fetchMyCoupons,
    fetchAvailableCoupons,
    useCoupon,
    calculateDiscount
  }
})
