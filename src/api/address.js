import api from './request'

export const addressApi = {
  // 获取地址列表
  getAddresses() {
    return api.get('/addresses')
  },

  // 获取地址详情
  getAddressDetail(addressId) {
    return api.get(`/addresses/${addressId}`)
  },

  // 新增地址
  createAddress(data) {
    return api.post('/addresses', data)
  },

  // 更新地址
  updateAddress(addressId, data) {
    return api.put(`/addresses/${addressId}`, data)
  },

  // 删除地址
  deleteAddress(addressId) {
    return api.delete(`/addresses/${addressId}`)
  },

  // 设为默认地址
  setDefaultAddress(addressId) {
    return api.put(`/addresses/${addressId}/default`)
  }
}
