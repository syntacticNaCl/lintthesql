-- update template
UPDATE content
   SET `value` = "<p>Hi!</p>
       <p>Your photos are ready!</p>
       <p>
           Gallery: ((gallery.url))<br/>
       </p>
       <p>You'll also need the following code to access your special privileges in the gallery:</p>
       <p>((gallery.admin_mode_pin))</p>
       <p>This code is meant only for you! Please do not share it with others.</p>
       <p>
           Thanks,<br/>
           ((brand.name))
       </p>"
 WHERE `key` = "studio.email_template.v2.default.event_pre_reg_release_to_event_contact";

-- update token; attempting to be as specific as possible but the IDs are different on PROD vs DEV
UPDATE email_template_token
   SET token = "((gallery.url))"
 WHERE token = "((gallery.admin_mode_url))"
   AND email_template_type_id = 16;

INSERT INTO schema_version (
    delta_id,
    direction,
    ran_on
) VALUES (
    1528404397,
    1,
    NOW()
);
