export async function apiReq(obj, endpoint, params) {

	var login_req = '';

	try {
		login_req = await obj.$axios.$post(`http://localhost:8000/${endpoint}`, params);
	}
	catch(error) {
		login_req = error.response.data;
	}
	return login_req;
}

export async function tokenAuth(obj) {
	var tokenReq = await apiReq(obj, 'api/v1/auth/jwt/verify');
	try {
		var refresh_token = tokenReq.refresh.access;
	}
	catch {
		var refresh_token = null;
	}
	if (tokenReq.status == 'ok') {
		return { status: true, refresh_token: refresh_token }
	}
	if (tokenReq.status == 'error') {
		return { status: false, refresh_token: refresh_token }
	}
}