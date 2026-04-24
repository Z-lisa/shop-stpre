import api from './request'

export const reviewApi = {
  // 获取评价列表
  getReviews(params) {
    return api.get('/reviews', { params })
  },

  // 创建评价
  createReview(data) {
    return api.post('/reviews', data)
  },

  // 更新评价
  updateReview(reviewId, data) {
    return api.put(`/reviews/${reviewId}`, data)
  },

  // 删除评价
  deleteReview(reviewId) {
    return api.delete(`/reviews/${reviewId}`)
  },

  // 点赞评价
  likeReview(reviewId) {
    return api.post(`/reviews/${reviewId}/like`)
  }
}
