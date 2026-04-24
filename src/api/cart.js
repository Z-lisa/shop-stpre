import api from './request'

export const cartApi = {
  // 获取购物车
  getCart() {
    return api.get('/cart')
  },

  // 添加到购物车
  addToCart(data) {
    return api.post('/cart/items', data)
  },

  // 更新购物车商品
  updateCartItem(itemId, data) {
    return api.put(`/cart/items/${itemId}`, data)
  },

  // 删除购物车商品
  deleteCartItem(itemId) {
    return api.delete(`/cart/items/${itemId}`)
  },

  // 清空购物车
  clearCart() {
    return api.delete('/cart')
  },

  // 切换选中状态
  toggleSelect(itemId) {
    return api.post(`/cart/select/${itemId}`)
  },

  // 全选/全不选
  selectAll(select = true) {
    return api.post('/cart/select-all', null, { params: { select } })
  }
}
