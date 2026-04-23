import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useUserStore } from './user'

export const useOrderStore = defineStore('order', () => {
  const userStore = useUserStore()
  
  // 根据用户类型存储不同的订单数据
  const getStorageKey = () => {
    return userStore.isGuest ? 'guest_orders' : 'orders'
  }
  
  const orders = ref(JSON.parse(localStorage.getItem(getStorageKey()) || '[]'))

  const saveToLocalStorage = () => {
    // 游客不保存订单数据
    if (userStore.isGuest) {
      return
    }
    localStorage.setItem(getStorageKey(), JSON.stringify(orders.value))
  }

  const pendingOrders = computed(() => {
    return orders.value.filter(order => order.status === 'pending')
  })

  const paidOrders = computed(() => {
    return orders.value.filter(order => order.status === 'paid')
  })

  const shippedOrders = computed(() => {
    return orders.value.filter(order => order.status === 'shipped')
  })

  const completedOrders = computed(() => {
    return orders.value.filter(order => order.status === 'completed')
  })

  const createOrder = (orderData) => {
    // 应用VIP折扣
    const originalPrice = orderData.totalPrice
    const discountedPrice = userStore.isVIP ? originalPrice * userStore.vipDiscount : originalPrice
    
    const newOrder = {
      id: 'BK' + Date.now().toString().slice(-10),
      items: orderData.items,
      totalPrice: discountedPrice,
      originalPrice: originalPrice, // 保存原价
      discount: userStore.isVIP ? userStore.vipDiscount : 1,
      isVIPOrder: userStore.isVIP,
      address: orderData.address,
      note: orderData.note || '', // 订单备注
      status: 'pending',
      createTime: new Date().toLocaleString('zh-CN', { 
        year: 'numeric', 
        month: '2-digit', 
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      }),
      payTime: null,
      shipTime: null,
      completeTime: null
    }
    orders.value.unshift(newOrder)
    saveToLocalStorage()
    return newOrder.id
  }

  const payOrder = (orderId, payMethod) => {
    const order = orders.value.find(o => o.id === orderId)
    if (order) {
      order.status = 'paid'
      order.payMethod = payMethod
      order.payTime = new Date().toLocaleString('zh-CN', { 
        year: 'numeric', 
        month: '2-digit', 
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      })
      
      // 更新用户消费金额（仅限登录用户）
      if (!userStore.isGuest) {
        userStore.updateSpending(order.totalPrice)
      }
      
      saveToLocalStorage()
    }
  }

  const shipOrder = (orderId) => {
    const order = orders.value.find(o => o.id === orderId)
    if (order) {
      order.status = 'shipped'
      order.shipTime = new Date().toLocaleString('zh-CN', { 
        year: 'numeric', 
        month: '2-digit', 
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      })
      saveToLocalStorage()
    }
  }

  const completeOrder = (orderId) => {
    const order = orders.value.find(o => o.id === orderId)
    if (order) {
      order.status = 'completed'
      order.completeTime = new Date().toLocaleString('zh-CN', { 
        year: 'numeric', 
        month: '2-digit', 
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      })
      saveToLocalStorage()
    }
  }

  const updateOrderAddress = (orderId, newAddress) => {
    const order = orders.value.find(o => o.id === orderId)
    if (order && order.status === 'pending') {
      order.address = newAddress
      saveToLocalStorage()
    }
  }

  const updateOrderItems = (orderId, newItems) => {
    const order = orders.value.find(o => o.id === orderId)
    if (order && order.status === 'pending') {
      order.items = newItems
      order.totalPrice = newItems.reduce((sum, item) => sum + item.price * item.quantity, 0)
      saveToLocalStorage()
    }
  }

  const getOrderById = (orderId) => {
    return orders.value.find(o => o.id === orderId)
  }

  const getOrdersByStatus = (status) => {
    if (status === 'all') return orders.value
    return orders.value.filter(o => o.status === status)
  }

  const deleteOrder = (orderId) => {
    const index = orders.value.findIndex(o => o.id === orderId)
    if (index > -1) {
      orders.value.splice(index, 1)
      saveToLocalStorage()
    }
  }

  return {
    orders,
    pendingOrders,
    paidOrders,
    shippedOrders,
    completedOrders,
    createOrder,
    payOrder,
    shipOrder,
    completeOrder,
    updateOrderAddress,
    updateOrderItems,
    getOrderById,
    getOrdersByStatus,
    deleteOrder
  }
})
