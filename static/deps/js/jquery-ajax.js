// When the html document is ready (drawn)
$(document).ready(function () {
    // we take the markup element with id jq-notification for ajax notifications into a variable
    var successMessage = $("#jq-notification");

    // We catch the click event on the add to cart button
    $(document).on("click", ".add-to-cart", function (e) {
        // Blocking its basic action
        e.preventDefault();

        // We take the counter element in the cart icon and take the value from there
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);

        // Getting the product id from the data-product-id attribute
        var product_id = $(this).data("product-id");

        // From the href attribute we take a link to the django controller
        var add_to_cart_url = $(this).attr("href");

        // make a post request via ajax without reloading the page
        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // message
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                // After 7 seconds we remove the message
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                // Increasing the number of items in the cart (rendered in the template)
                cartCount++;
                goodsInCartCount.text(cartCount);

                // We change the contents of the cart to the response from django (a new rendered fragment of the cart markup)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },

            error: function (data) {
                console.log("Error adding item to cart");
            },
        });
    });


    // We catch the event of a click on the button to remove an item from the cart
    $(document).on("click", ".remove-from-cart", function (e) {
        // Blocking its basic action
        e.preventDefault();

        // We take the counter element in the cart icon and take the value from there
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);

        // Getting the cart id from the data-cart-id attribute
        var cart_id = $(this).data("cart-id");
        // From the href attribute we take a link to the django controller
        var remove_from_cart = $(this).attr("href");

        // make a post request via ajax without reloading the page
        $.ajax({

            type: "POST",
            url: remove_from_cart,
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // message
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                // After 7 seconds we remove the message
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                // Reducing the number of items in the cart (rendering)
                cartCount -= data.quantity_deleted;
                goodsInCartCount.text(cartCount);

                // We change the contents of the cart to the response from django (a new rendered fragment of the cart markup)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },

            error: function (data) {
                console.log("Error adding item to cart");
            },
        });
    });


    // Now + - quantity of goods
    // Event handler for decrementing value
    $(document).on("click", ".decrement", function () {
        // We take the link to the django controller from the data-cart-change-url attribute
        var url = $(this).data("cart-change-url");
        // We take the cart id from the data-cart-id attribute
        var cartID = $(this).data("cart-id");
        // We are looking for the nearest input with quantity
        var $input = $(this).closest('.input-group').find('.number');
        // We take the value of the quantity of goods
        var currentValue = parseInt($input.val());
        // If there is more than one quantity, then only do -1
        if (currentValue > 1) {
            $input.val(currentValue - 1);
            // Run the function defined below
            // with arguments (card id, new quantity, quantity decreased or increased, url)
            updateCart(cartID, currentValue - 1, -1, url);
        }
    });

    // Event handler for increasing value
    $(document).on("click", ".increment", function () {
        // We take the link to the django controller from the data-cart-change-url attribute
        var url = $(this).data("cart-change-url");
        // We take the cart id from the data-cart-id attribute
        var cartID = $(this).data("cart-id");
        // We are looking for the nearest input with quantity
        var $input = $(this).closest('.input-group').find('.number');
        // We take the value of the quantity of goods
        var currentValue = parseInt($input.val());

        $input.val(currentValue + 1);

        // Run the function defined below
        // with arguments (card id, new quantity, quantity decreased or increased, url)
        updateCart(cartID, currentValue + 1, 1, url);
    });

    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {
                 // message
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                 // After 7 seconds we remove the message
                setTimeout(function () {
                     successMessage.fadeOut(400);
                }, 7000);

                // Changing the number of items in the cart
                var goodsInCartCount = $("#goods-in-cart-count");
                var cartCount = parseInt(goodsInCartCount.text() || 0);
                cartCount += change;
                goodsInCartCount.text(cartCount);

                // Changing the contents of the cart
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },
            error: function (data) {
                console.log("Error adding item to cart");
            },
        });
    }

    var notification = $('#notification');
    // and after 7 seconds remove
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }

    // When you click on the cart icon, a pop-up (modal) window opens
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    // Click on the button to close the cart window
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Event handler for radio button selecting delivery method
    $("input[name='requires_delivery']").change(function () {
        var selectedValue = $(this).val();
        // Hiding or displaying the delivery address input
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });

});