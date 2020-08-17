SELECT `post_title`, `post_date_gmt`, `post_modified_gmt`, `post_name`, `id`, `wp_term_taxonomy`.description, `wp_term_taxonomy`.taxonomy, `wp_terms`.slug, `wp_terms`.name, `post_content`
FROM `wp_posts`
LEFT JOIN `wp_term_relationships` ON `wp_term_relationships`.object_id = wp_posts.id
LEFT JOIN `wp_term_taxonomy` ON `wp_term_taxonomy`.term_taxonomy_id = `wp_term_relationships`.term_taxonomy_id
LEFT JOIN `wp_terms` ON `wp_terms`.term_id = `wp_term_taxonomy`.term_id
WHERE wp_posts.post_type = 'post'
ORDER BY `wp_posts`.id ASC