import api from './request'

export const favoriteApi = {
  // 获取收藏列表
  getFavorites() {
    return api.get('/favorites')
  },

  // 添加收藏
  addFavorite(productId) {
    return api.post(`/favorites/${productId}`)
  },

  // 取消收藏
  removeFavorite(productId) {
    return api.delete(`/favorites/${productId}`)
  }
}
