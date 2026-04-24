import api from './request'

export const orderApi = {
  // 获取订单列表
  getOrders(params) {
    return api.get('/orders', { params })
  },

  // 获取订单详情
  getOrderDetail(orderId) {
    return api.get(`/orders/${orderId}`)
  },

  // 创建订单
  createOrder(data) {
    return api.post('/orders', data)
  },

  // 支付订单
  payOrder(orderId, payMethod) {
    return api.post(`/orders/${orderId}/pay`, null, {
      params: { pay_method: payMethod }
    })
  },

  // 取消订单
  cancelOrder(orderId) {
    return api.post(`/orders/${orderId}/cancel`)
  },

  // 确认收货
  confirmOrder(orderId) {
    return api.post(`/orders/${orderId}/confirm`)
  }
}
