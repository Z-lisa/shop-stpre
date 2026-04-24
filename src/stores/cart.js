import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { cartApi } from '@/api/cart'

export const useCartStore = defineStore('cart', () => {
  const cartItems = ref([])
  const loading = ref(false)

  // 从 API 加载购物车
  const fetchCart = async () => {
    loading.value = true
    try {
      const data = await cartApi.getCart()
      cartItems.value = data.items || []
      return data
    } catch (error) {
      console.error('获取购物车失败:', error)
      cartItems.value = []
      return { items: [], total_items: 0, total_price: 0 }
    } finally {
      loading.value = false
    }
  }

  const totalItems = computed(() => {
    return cartItems.value.reduce((sum, item) => sum + item.quantity, 0)
  })

  const totalPrice = computed(() => {
    return cartItems.value.reduce((sum, item) => sum + item.product.price * item.quantity, 0)
  })

  const selectedTotal = computed(() => {
    return cartItems.value
      .filter(item => item.is_selected)
      .reduce((sum, item) => sum + item.product.price * item.quantity, 0)
  })

  const selectedCount = computed(() => {
    return cartItems.value
      .filter(item => item.is_selected)
      .reduce((sum, item) => sum + item.quantity, 0)
  })

  const isAllSelected = computed(() => {
    return cartItems.value.length > 0 && 
           cartItems.value.every(item => item.is_selected)
  })

  // 选中的商品ID列表
  const selectedItems = computed(() => {
    return cartItems.value
      .filter(item => item.is_selected)
      .map(item => item.id)
  })

  // 添加到购物车
  const addToCart = async (productId, quantity = 1, size = null) => {
    const data = await cartApi.addToCart({
      product_id: productId,
      quantity,
      size
    })
    await fetchCart()
    return data
  }

  // 从购物车删除
  const removeFromCart = async (itemId) => {
    await cartApi.deleteCartItem(itemId)
    await fetchCart()
  }

  // 更新数量
  const updateQuantity = async (itemId, quantity) => {
    await cartApi.updateCartItem(itemId, { quantity })
    await fetchCart()
  }

  // 切换选中状态
  const toggleSelect = async (itemId) => {
    await cartApi.toggleSelect(itemId)
    await fetchCart()
  }

  // 全选/全不选
  const selectAll = async () => {
    const select = !isAllSelected.value
    await cartApi.selectAll(select)
    await fetchCart()
  }

  // 清空购物车
  const clearCart = async () => {
    await cartApi.clearCart()
    cartItems.value = []
  }

  // 获取选中的商品
  const getSelectedItems = () => {
    return cartItems.value.filter(item => item.is_selected)
  }

  // 立即购买：添加商品并标记为选中，其他商品取消选中
  const buyNow = async (productId, quantity = 1, size = null) => {
    // 先取消所有商品的选中状态
    if (cartItems.value.length > 0) {
      await cartApi.selectAll(false)
    }
    // 添加商品到购物车
    const data = await cartApi.addToCart({
      product_id: productId,
      quantity,
      size
    })
    // 重新加载购物车获取最新数据
    await fetchCart()
    // 选中新添加的商品（最后一个）
    const newItem = cartItems.value[cartItems.value.length - 1]
    if (newItem) {
      await cartApi.toggleSelect(newItem.id)
      await fetchCart()
    }
    return data
  }

  return {
    cartItems,
    loading,
    totalItems,
    totalPrice,
    selectedTotal,
    selectedCount,
    isAllSelected,
    selectedItems,
    fetchCart,
    addToCart,
    removeFromCart,
    updateQuantity,
    toggleSelect,
    selectAll,
    clearCart,
    getSelectedItems,
    buyNow
  }
})
