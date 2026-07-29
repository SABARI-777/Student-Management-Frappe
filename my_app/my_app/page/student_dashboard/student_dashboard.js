frappe.pages['student-dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'STUDENT',
		single_column: true
	});
	page.add_inner_button("Refresh", function () {
    frappe.msgprint("Refreshing");

});
	$(page.body).html(`
    <h2>Welcome</h2>

    <button class="btn btn-primary">
        Click Me
    </button>
`);
}