import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useReviewsStore = defineStore('reviews', () => {
  // 评价数据存储，按书籍ID分组
  const bookReviews = ref({})

  // 获取某本书的评价列表
  const getBookReviews = (bookId) => {
    return bookReviews.value[bookId] || []
  }

  // 添加评价
  const addReview = (bookId, review) => {
    if (!bookReviews.value[bookId]) {
      bookReviews.value[bookId] = []
    }
    
    const newReview = {
      user: '匿名用户',
      rating: review.rating,
      content: review.content,
      date: new Date().toISOString().split('T')[0],
      likes: 0
    }
    
    bookReviews.value[bookId].unshift(newReview)
    return newReview
  }

  // 点赞评价
  const likeReview = (bookId, reviewIndex) => {
    if (bookReviews.value[bookId] && bookReviews.value[bookId][reviewIndex]) {
      bookReviews.value[bookId][reviewIndex].likes++
    }
  }

  return {
    bookReviews,
    getBookReviews,
    addReview,
    likeReview
  }
})
