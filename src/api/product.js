import api from './request'

export const productApi = {
  // 获取商品列表
  getProducts(params) {
    return api.get('/products', { params })
  },

  // 获取商品详情
  getProductDetail(id) {
    return api.get(`/products/${id}`)
  },

  // 获取推荐商品
  getRecommendProducts(id, limit = 6) {
    return api.get(`/products/${id}/recommend`, { params: { limit } })
  },

  // 获取分类列表
  getCategories(parentId = null) {
    return api.get('/categories', { params: { parent_id: parentId } })
  },

  // 获取分类树
  getCategoryTree() {
    return api.get('/categories/tree')
  }
}
