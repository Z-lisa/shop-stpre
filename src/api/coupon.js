import api from './request'

export const couponApi = {
  // 获取优惠券列表
  getCoupons() {
    return api.get('/coupons')
  },

  // 领取优惠券
  claimCoupon(couponId) {
    return api.post(`/coupons/${couponId}/claim`)
  },

  // 获取我的优惠券
  getMyCoupons() {
    return api.get('/coupons/my')
  },

  // 获取可用优惠券
  getAvailableCoupons() {
    return api.get('/coupons/available')
  }
}
